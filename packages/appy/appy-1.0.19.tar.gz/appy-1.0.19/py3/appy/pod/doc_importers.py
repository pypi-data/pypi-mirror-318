#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# Copyright (C) 2007-2024 Gaetan Delannay

# This file is part of Appy.

# Appy is free software: you can redistribute it and/or modify it under the
# terms of the GNU General Public License as published by the Free Software
# Foundation, either version 3 of the License, or (at your option) any later
# version.

# Appy is distributed in the hope that it will be useful, but WITHOUT ANY
# WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR
# A PARTICULAR PURPOSE. See the GNU General Public License for more details.

# You should have received a copy of the GNU General Public License along with
# Appy. If not, see <http://www.gnu.org/licenses/>.

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
import os, os.path, re, stat, shutil, struct, urllib.parse, base64, io

import appy.pod
from appy import utils
from appy.utils import css, imghdr
from appy.pod import PodError, getUuid
from appy.utils.client import Resource
from appy.model.utils import Object as O
from appy.pod.metadata import MetadataReader
from appy.pod.odf_parser import OdfEnvironment
from appy.utils.path import getOsTempFolder, getTempFileName

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
FILE_KO  = "'%s' does not exist or is not a file."
GS_KO    = 'A PDF file could not be converted into images. Please ensure ' \
           'Ghostscript (gs) is installed on your system and the "gs" ' \
           'program is in the path.'
PDF_ERR  = 'ConvertImporter error while converting a doc to PDF: %s.'

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
n = None

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
class DocImporter:
    '''Base class used for importing external content into a pod template (an
       image, another pod template, another odt document...'''

    def __init__(self, content, at, format, renderer):
        self.content = content
        self.renderer = renderer
        # If content is None, p_at tells us where to find it (file path, url...)
        self.at = at
        # Check and standardize p_at
        self.format = format
        if at:
            self.at = self.checkAt(at)
        self.res = ''
        self.ns = renderer.currentParser.env.namespaces
        # Unpack some useful namespaces
        self.textNs = self.ns[OdfEnvironment.NS_TEXT]
        self.linkNs = self.ns[OdfEnvironment.NS_XLINK]
        self.drawNs = self.ns[OdfEnvironment.NS_DRAW]
        self.svgNs = self.ns[OdfEnvironment.NS_SVG]
        self.tempFolder = renderer.tempFolder
        self.importFolder = self.getImportFolder()
        # Create the import folder if it does not exist
        if not os.path.exists(self.importFolder): os.mkdir(self.importFolder)
        self.importPath = self.getImportPath()
        # A link to the global fileNames dict (explained in renderer.py)
        self.fileNames = renderer.fileNames
        if self.at:
            # Move the file within the ODT, if it is an image and if this image
            # has not already been imported.
            self.importPath = self.moveFile()
        else:
            # The file content (in self.content) must be dumped in a temp file
            # first. It may be binary or a file handler.
            cont = self.content
            cont = cont.read() if isinstance(cont, io.IOBase) else cont
            with open(self.importPath, 'wb') as f: f.write(cont)
        # Some importers add specific attrs via m_init

    def checkAt(self, at, raiseOnError=True):
        '''Check and apply some transform to p_at'''
        # Resolve relative path
        if at.startswith('./'): at = os.path.join(os.getcwd(), at[2:])
        # Checks that p_at corresponds to an existing file if given
        if raiseOnError and not os.path.isfile(at):
            raise PodError(FILE_KO % at)
        return at

    def getImportFolder(self):
        '''This method gives the path where to dump the content of the document
           or image. In the case of a document it is a temp folder; in the case
           of an image it is a folder within the ODT result.'''
        return '%s/docImports' % self.tempFolder # For most importers

    def getImportPath(self):
        '''Gets the path name of the file to dump on disk (within the ODT for
           images, in a temp folder for docs).'''
        format = self.format
        if not format or format == 'image':
            at = self.at
            if not at or at.startswith('http') or not os.path.exists(at):
                # It is not possible yet to determine the format (will be done
                # later).
                self.format = ''
            else:
                self.format = os.path.splitext(at)[1][1:]
        fileName = '%s.%s' % (getUuid(), self.format)
        return os.path.abspath('%s/%s' % (self.importFolder, fileName))

    def moveFile(self):
        '''In the case "self.at" was used, we may want to move the file at
           self.at within the ODT result in self.importPath (for images) or do
           nothing (for docs). In the latter case, the file to import stays
           at self.at, and is not copied into self.importPath. So the previously
           computed self.importPath is not used at all.'''
        return self.at

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
class OdtImporter(DocImporter):
    '''This class allows to import the content of another ODT document into a
       pod template.'''

    # POD manages page breaks by inserting a paragraph whose style inserts a
    # page break before or after it.
    pageBreakTemplate = '<text:p text:style-name="podPageBreak%s"></text:p>'
    pageBreaks = O(before=pageBreakTemplate % 'Before',
                   after=pageBreakTemplate % 'After',
                   beforeDuplex=pageBreakTemplate % 'BeforeDuplex')

    def init(self, pageBreakBefore, pageBreakAfter):
        '''OdtImporter-specific constructor'''
        self.pageBreakBefore = pageBreakBefore
        self.pageBreakAfter = pageBreakAfter

    def getPageBreakAfterType(self):
        '''After sub-document insertion, must we insert a page break of type
           "after" or "before"?'''
        if self.pageBreakAfter == 'duplex':
            # Read metadata about the sub-ODT, containing its number of pages
            metadata = MetadataReader(self.importPath).run()
            odd = (metadata.pagecount % 2) == 1
            # Inserting a page break of type "before" will force an additional
            # page break, while inserting a page break of type "after" will only
            # insert a page break if additional content is found after the
            # paragraph onto which the page break style is applied.
            r = odd and 'beforeDuplex' or 'after'
        else:
            r = 'after'
        return r

    def run(self):
        '''Import the content of a sub-ODT document'''
        # Insert a page break before importing the doc if needed
        if self.pageBreakBefore: self.res += self.pageBreaks.before
        # Import the external odt document
        name = getUuid(removeDots=True, prefix='PodSect')
        self.res += '<%s:section %s:name="%s">' \
                    '<%s:section-source %s:href="file://%s" ' \
                    '%s:filter-name="writer8"/></%s:section>' % (
                        self.textNs, self.textNs, name, self.textNs,
                        self.linkNs, self.importPath, self.textNs, self.textNs)
        # Insert (a) page break(s) after importing the doc if needed
        if self.pageBreakAfter:
            type = self.getPageBreakAfterType()
            self.res += getattr(self.pageBreaks, type)
            # Note that if there is no more document content after the last page
            # break, it will not be visible.
        return self.res

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
class PodImporter(DocImporter):
    '''Imports the result of applying another POD template, into the current POD
       result.'''

    def mustStream(self):
        '''Returns "in" if communication with LibreOffice must be performed via
           streams.'''
        ren = self.renderer
        # The default value is the one from the main renderer
        default = ren.stream
        # Must we communicate with LO via streams ?
        stream = (default in (True, 'in')) or \
                 (default == 'auto' and ren.loPool.server != 'localhost')
        # If the global result must be streamed, for this sub-pod, stream must
        # be "in": this way, the output is written on disk, on the distant LO
        # machine. Then, when we will, via the OdtImporter that will be called
        # just after this PodImporter, specify the sub-pod to include, the
        # distant LO will be able to read it from is own disk.
        return stream and 'in' or default

    def init(self, context, pageBreakBefore, pageBreakAfter,
             managePageStyles, resolveFields, forceOoCall):
        '''PodImporter-specific constructor'''
        self.context = context
        self.pageBreakBefore = pageBreakBefore
        self.pageBreakAfter = pageBreakAfter
        self.managePageStyles = managePageStyles
        self.resolveFields = resolveFields
        # Must we communicate with LO via streams ?
        self.stream = self.mustStream()
        # Force LO call if:
        # (a) fields must be resolved ;
        # (b) if we are inserting sub-documents in "duplex" mode. Indeed, in
        #     this latter case, we will need to know the exact number of pages
        #     for every sub-document. We will call LO for that purpose: it will
        #     produce correct document statistics within meta.xml, which is not
        #     the case for an ODT document produced by POD without forcing OO
        #     call (stats are those from the document template and not from the
        #     pod result) ;
        # (c) LO is on a distant machine. In that case, forcing OO call allows
        #     to transmit the sub-pod to the distant machine, ready to be
        #     incorpotared by the distant LO in the main pod.
        if pageBreakAfter == 'duplex' or resolveFields or self.stream == 'in':
            force = True
        else:
            # Inherit from the parent renderer's value or get a specific value
            renderer = self.renderer
            if forceOoCall == renderer.INHERIT:
                force = renderer.forceOoCall
            else:
                # Else, keep the value as passed to p_self's constructor
                force = forceOoCall
        self.forceOoCall = force

    def run(self):
        # This feature is only available in the open source version
        if utils.commercial: raise utils.CommercialError()
        r = self.renderer
        # Define where to store the pod result in the temp folder. If we must
        # stream the result, the temp folder will be on a distant machine, so it
        # must be at the root of the OS temp folder.
        stream = self.stream
        base = getOsTempFolder() if stream == 'in' else self.getImportFolder()
        resOdt = os.path.join(base, '%s.odt' % getUuid())
        # The POD template is in self.importPath
        template = self.importPath
        # Re-use an existing renderer if we have one that has already generated
        # a result based on this template.
        renderer = r.children.get(template)
        if not renderer:
            renderer = r.clone(template, self.context, resOdt, stream=stream,
              forceOoCall=self.forceOoCall,
              managePageStyles=self.managePageStyles,
              resolveFields=self.resolveFields, metadata=False,
              deleteTempFolder=False, loPool=r.loPool)
            renderer.stylesManager.stylesMapping = r.stylesManager.stylesMapping
            # Add this renderer to the list of child renderers on the parent
            r.children[template] = renderer
        else:
            # Recycle this renderer and set him a new result
            renderer.reinit(resOdt, self.context)
        renderer.run()
        # The POD result is in "resOdt". Import it into the main POD result
        # using an OdtImporter.
        odtImporter = OdtImporter(n, resOdt, 'odt', self.renderer)
        odtImporter.init(self.pageBreakBefore, self.pageBreakAfter)
        return odtImporter.run()

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
class PdfImporter(DocImporter):
    '''This class allows to import the content of a PDF file into a pod
       template. It calls gs to split the PDF into images and calls the
       ImageImporter for importing it into the result.'''
    # Ghostscript devices that can be used for converting PDFs into images
    gsDevices = {'jpeg': 'jpg', 'jpeggray': 'jpg',
                 'png16m': 'png', 'pnggray': 'png'}

    def run(self):
        # This feature is only available in the open source version
        if utils.commercial: raise utils.CommercialError()
        imagePrefix = os.path.splitext(os.path.basename(self.importPath))[0]
        # Split the PDF into images with Ghostscript. Create a sub-folder in the
        # OS temp folder to store those images.
        imagesFolder = getOsTempFolder(sub=True)
        device = 'png16m'
        ext = PdfImporter.gsDevices[device]
        dpi = '125'
        cmd = ['gs', '-dSAFER', '-dNOPAUSE', '-dBATCH', f'-sDEVICE={device}',
               f'-r{dpi}', '-dTextAlphaBits=4', '-dGraphicsAlphaBits=4',
               f'-sOutputFile={imagesFolder}/{imagePrefix}%d.{ext}',
               self.importPath]
        utils.executeCommand(cmd)
        # Check that at least one image was generated
        succeeded = False
        firstImage = f'{imagePrefix}1.{ext}'
        for fileName in os.listdir(imagesFolder):
            if fileName == firstImage:
                succeeded = True
                break
        if not succeeded: raise PodError(GS_KO)
        # Insert images into the result
        noMoreImages = False
        i = 0
        while not noMoreImages:
            i += 1
            nextImage = f'{imagesFolder}/{imagePrefix}{i}.{ext}'
            if os.path.exists(nextImage):
                # Use internally an Image importer for doing this job
                imgImporter = ImageImporter(n, nextImage, ext, self.renderer)
                imgImporter.init('as-char',True,n,n,'page','page',n,True,n)
                self.res += imgImporter.run()
                os.remove(nextImage)
            else:
                noMoreImages = True
        os.rmdir(imagesFolder)
        return self.res

    #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    #                       Other useful gs commands
    #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    # Convert a PDF from colored to grayscale
    #gs -sOutputFile=grayscale.pdf -sDEVICE=pdfwrite
    #   -sColorConversionStrategy=Gray -dProcessColorModel=/DeviceGray
    #   -dCompatibilityLevel=1.4 -dNOPAUSE -dBATCH colored.pdf

    # Downsample inner images to produce a smaller PDF
    #gs -sOutputFile=smaller.pdf -sDEVICE=pdfwrite
    #   -dCompatibilityLevel=1.4 -dPDFSETTINGS=/screen
    #   -dNOPAUSE -dBATCH some.pdf

    # The "-dPDFSETTINGS=/screen is a shorthand for:
    #-dDownsampleColorImages=true \
    #-dDownsampleGrayImages=true \
    #-dDownsampleMonoImages=true \
    #-dColorImageResolution=72 \
    #-dGrayImageResolution=72 \
    #-dMonoImageResolution=72

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
class ConvertImporter(DocImporter):
    '''This class allows to import the content of any file that LibreOffice (LO)
       can convert into PDF: doc(x), rtf, xls(x)... It first calls LO to convert
       the document into PDF, then calls a PdfImporter.'''
    def run(self):
        # This feature is only available in the open source version
        if utils.commercial: raise utils.CommercialError()
        # Convert the document into PDF with LibreOffice
        pdfFile = getTempFileName(extension='pdf')
        output = self.renderer.callLibreOffice(self.importPath,
                                               outputName=pdfFile)
        if output: raise PodError(PDF_ERR % output)
        # Launch a PdfImporter to import this PDF into the POD result
        pdfImporter = PdfImporter(None, pdfFile, 'pdf', self.renderer)
        return pdfImporter.run()

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
class Image:
    '''Represents an image on disk. This class is used to detect the image type
       and size.'''
    jpgTypes = ('jpg', 'jpeg')

    def __init__(self, path, format, unit='cm'):
        self.path = path # The image absolute path on disk
        self.format = format or imghdr.what(path)
        # Determine image size in pixels (again, by reading its first bytes)
        self.width, self.height = self.getSizeIn(unit)

    def getSizeIn(self, unit='cm'):
        '''Reads the first bytes from the image on disk to get its size'''
        x = y = None
        # Get the file format from the file name of absent
        format = self.format or os.path.splitext(self.path)[1][1:]
        # Read the file on disk
        f = open(self.path, 'rb')
        if format in Image.jpgTypes:
            # Dummy read to skip header ID
            f.read(2)
            while True:
                # Extract the segment header
                marker, code, length = struct.unpack("!BBH", f.read(4))
                # Verify that it's a valid segment
                if marker != 0xFF:
                    # No JPEG marker
                    break
                elif code >= 0xC0 and code <= 0xC3:
                    # Segments that contain size info
                    y, x = struct.unpack("!xHH", f.read(5))
                    break
                else:
                    # Dummy read to skip over data
                    f.read(length-2)
        elif format == 'png':
            # Dummy read to skip header data
            head = f.read(24)
            check = struct.unpack('>i', head[4:8])[0]
            if check == 0x0d0a1a0a:
                x, y = struct.unpack('>ii', head[16:24])
        elif format == 'gif':
            imgType = f.read(6)
            buf = f.read(5)
            if len(buf) == 5:
                # else: invalid/corrupted GIF (bad header)
                x, y, u = struct.unpack("<HHB", buf)
        f.close()
        if (x and y) and (unit == 'cm'):
            return float(x)/css.px2cm, float(y)/css.px2cm
        else:
            # Return the size, in pixels, or as a tuple (None, None) if
            # uncomputable.
            return x, y

#  - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
class ImageImporter(DocImporter):
    '''This class allows to import into the ODT result an image stored
       externally.'''

    # Ways to anchor images in an ODF document
    anchorTypes = ('page', 'paragraph', 'char', 'as-char')
    WRONG_ANCHOR = 'Wrong anchor. Valid values for anchors are: %s.'

    # The folder, within an unzipped ODF file, containing images
    pictFolder = f'{os.sep}Pictures{os.sep}'

    # Path of a replacement image, to use when the image to import is not found
    imageNotFound = os.path.join(os.path.dirname(appy.pod.__file__),
                                 'imageNotFound.jpg')

    # Regular expression for finding orientation within EXIF meta-data
    orientationRex = re.compile(r'exif:Orientation\s*=\s*(\d+)')

    def isImage(self, response):
        '''Cheks that the p_response received after a HTTP GET supposed to
           retrieve an image actually contains an image.'''
        if not response or (response.code != 200): return
        # Check p_response's content type
        type = response.headers.get('content-type')
        # The most frequent case: the HTTP GET returns an error page, ie, if the
        # image URL requires authentication.
        if type and not type.startswith('image/'): return
        return True

    def checkAt(self, at):
        '''Do not raise an exception when p_at does not correspond to an
           existing file. We will dump a replacement image instead.'''
        at = DocImporter.checkAt(self, at, raiseOnError=False)
        if at.startswith('http'):
            # Try to get the image via the "findImage" function
            fun = self.renderer.findImage
            if fun:
                path = fun(at)
                if path: return path
            # Try to get the image via a HTTP request
            try:
                response = Resource(at).get(at, followRedirect=False)
            except Resource.Error as err:
                response = None # Can't get the distant image
            if self.isImage(response):
                # Remember the response
                self.httpResponse = response
                return at
            # If we are here, the image could not be found
            self.format = 'jpg'
            return self.imageNotFound
        elif at.startswith('data:'):
            # The image content and type are embedded in p_at, which comes from
            # the "src" attribute of a HTML "img" tag of the form:
            #              "data:<mimeType>;base64,<base64 content>"
            mimeType = at[5:at.index(';')]
            # The MIME type may be "image/*". In that case, set "img" as virtual
            # format; the real format will be detected once the file will be
            # dumped to disk.
            self.format = utils.mimeTypesExts.get(mimeType) or 'img'
            content = at[at.index(',')+1:]
            # Decode the base64 content and store it in a temp file on disk
            content = base64.b64decode(content)
            fileName = getTempFileName(extension=self.format)
            f = open(fileName, 'wb')
            f.write(content)
            f.close()
            if self.format == 'img':
                self.format = imghdr.what(fileName)
            return fileName
        else:
            if at.startswith('file://'): at = at[7:]
            if not os.path.isfile(at):
                self.format = 'jpg'
                at = self.imageNotFound
            elif self.format == 'image':
                # Read its format by reading its first bytes
                self.format = imghdr.what(str(at))
            return at

    def getImportFolder(self):
        return os.path.join(self.tempFolder, 'unzip', 'Pictures')

    def moveFile(self):
        '''Copies file at self.at into the ODT file at self.importPath'''
        at = self.at
        importPath = self.importPath
        # Has this image already been imported ?
        for imagePath, imageAt in self.fileNames.items():
            if imageAt == at: # Yes
                i = importPath.rfind(self.pictFolder) + 1
                return importPath[:i] + imagePath
        # The image has not already been imported: copy it
        if not at.startswith('http'):
            shutil.copy(at, importPath)
            # Ensure we can modify the image (with ImageMagick)
            os.chmod(importPath, stat.S_IREAD | stat.S_IWRITE)
            return importPath
        # The image has (maybe) been retrieved from a HTTP GET
        response = getattr(self, 'httpResponse', None)
        if response:
            # Retrieve the image format
            format = response.headers['Content-Type']
            if format in utils.mimeTypesExts:
                # At last, I can get the file format
                self.format = utils.mimeTypesExts[format]
                importPath += self.format
                f = open(importPath, 'wb')
                f.write(response.body)
                f.close()
                return importPath

    def manageExif(self):
        '''Read, with ImageMagick, EXIF metadata in the image, and apply a
           rotation (still with ImageMagick) if required.'''
        # Indeed, LO will not interpret EXIF metadata when reading the image
        path = self.importPath
        cmd = ['identify', '-format', '%[EXIF:*]', path]
        out = utils.ImageMagick.run(cmd)
        if out:
            match = self.orientationRex.search(out)
            if match:
                #code = int(match.group(1)) # "auto-orient" manages all codes
                utils.ImageMagick.convert(path, '-auto-orient')

    def init(self, anchor, wrapInPara, size, sizeUnit, maxWidth, maxHeight,
             cssAttrs, keepRatio, convertOptions):
        '''ImageImporter-specific constructor'''
        # Initialise anchor
        if anchor not in self.anchorTypes:
            raise PodError(self.WRONG_ANCHOR % str(self.anchorTypes))
        self.anchor = anchor
        self.wrapInPara = wrapInPara
        self.size = size
        self.sizeUnit = sizeUnit
        pageLayout = self.renderer.stylesManager.pageLayout
        if maxWidth == 'page':
            maxWidth = pageLayout.getWidth()
        self.maxWidth = maxWidth
        if maxHeight == 'page':
            maxHeight = pageLayout.getHeight()
        self.maxHeight = maxHeight
        self.keepRatio = keepRatio
        self.convertOptions = convertOptions
        # CSS attributes
        self.cssAttrs = cssAttrs
        if cssAttrs:
            w = getattr(self.cssAttrs, 'width', None)
            h = getattr(self.cssAttrs, 'height', None)
            if w and h:
                self.sizeUnit = w.unit
                self.size = (w.value, h.value)
        # Manage EXIF tags when relevant
        if self.renderer.rotateImages: self.manageExif()
        # Call ImageMagick to perform a custom conversion if required
        options = self.convertOptions
        image = None
        transformed = False
        if options:
            # This feature is only available in the open source version
            if utils.commercial: raise utils.CommercialError()
            if callable(options): # It is a function
                image = Image(self.importPath, self.format)
                options = self.convertOptions(image)
            if options:
                utils.ImageMagick.convert(self.importPath, options)
                transformed = True
        # Avoid creating an Image instance twice if no transformation occurred
        if image and not transformed:
            self.image = image
        else:
            self.image = Image(self.importPath, self.format)

    def applyMax(self, width, height):
        '''Return a tuple (width, height), potentially modified w.r.t. p_width
           and p_height, to take care of p_self.maxWidth & p_self.maxHeight.'''
        # Apply max width
        maxW = self.maxWidth
        if maxW and width > maxW:
            ratio = maxW / width
            width = maxW
            # Even if the width/height ratio must not be kept, in this case,
            # nevertheless apply it.
            height *= ratio
        # Apply max height
        maxH = self.maxHeight
        if maxH and height > maxH:
            ratio = maxH / height
            height = maxH
            # Even if keepRatio is False, in that case, nevertheless apply the
            # ratio on height, too.
            width *= ratio
        return width, height

    def getImageSize(self):
        '''Get or compute the image size and returns the corresponding ODF
           attributes specifying image width and height expressed in cm.'''
        # Compute image size, in cm
        width, height = self.image.width, self.image.height
        keepRatio = self.keepRatio
        if self.size:
            # Apply a percentage when p_self.sizeUnit is 'pc'
            if self.sizeUnit == 'pc':
                # If width or height could not be computed, it is impossible
                if not width or not height: return ''
                if keepRatio:
                    ratioW = ratioH = float(self.size[0]) / 100
                else:
                    ratioW = float(self.size[0]) / 100
                    ratioH = float(self.size[1]) / 100
                width = width * ratioW
                height = height * ratioH
            else:
                # Get, from p_self.size, required width and height, and convert
                # it to cm when relevant.
                w, h = self.size
                if self.sizeUnit == 'px':
                    try:
                        w = float(w) / css.px2cm
                        h = float(h) / css.px2cm
                    except ValueError:
                        # Wrong values: use v_width and v_height
                        w = width
                        h = height
                # Use (w, h) as is if we don't care about keeping image ratio or
                # if we couldn't determine image's width or height.
                if (not width or not height) or not keepRatio:
                    width, height = w, h
                else:
                    # Compute height and width ratios and apply the minimum
                    # ratio to both width and height.
                    ratio = min(w/width, h/height)
                    width *= ratio
                    height *= ratio
        if not width or not height: return ''
        # Take care of max width & height if specified
        width, height = self.applyMax(width, height)
        # Return the ODF attributes
        s = self.svgNs
        return f' {s}:width="{width:.6f}cm" {s}:height="{height:.6f}cm"'

    def run(self):
        # Some shorcuts for the used xml namespaces
        d = self.drawNs
        t = self.textNs
        x = self.linkNs
        # Compute path to image
        i = self.importPath.rfind(self.pictFolder)
        imagePath = self.importPath[i+1:].replace('\\', '/')
        self.fileNames[imagePath] = self.at
        # Compute image alignment if CSS attr "float" is specified
        floatValue = getattr(self.cssAttrs, 'float', None)
        if floatValue:
            floatValue = floatValue.value.capitalize()
            styleInfo = f'{d}:style-name="podImage{floatValue}" '
            self.anchor = 'char'
        else:
            styleInfo = ''
        name = getUuid(prefix='I', removeDots=True)
        # p_self.anchor is specific to an ODT template. If the image is to be
        # dumped into an ODS result, it will have implicit "to-cell" anchor.
        if self.renderer.templateType == 'ods':
            anchor = ''
        else:
            anchor = f' {t}:anchor-type="{self.anchor}"'
        image = f'<{d}:frame {styleInfo}{d}:name="{name}" {d}:z-index="0" ' \
                f'{anchor}{self.getImageSize()}><{d}:image {x}:type="simple" ' \
                f'{x}:show="embed" {x}:href="{imagePath}" ' \
                f'{x}:actuate="onLoad"/></{d}:frame>'
        if hasattr(self, 'wrapInPara') and self.wrapInPara:
            style = f' text:style-name="{self.wrapInPara}"' \
                    if isinstance(self.wrapInPara, str) else ''
            image = f'<{t}:p{style}>{image}</{t}:p>'
        self.res += image
        return self.res
#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

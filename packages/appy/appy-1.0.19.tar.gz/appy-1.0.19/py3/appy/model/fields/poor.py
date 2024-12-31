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

#  - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
from appy.px import Px
from appy.xml.cleaner import Cleaner
from appy.model.fields.rich import Rich
from appy.utils import string as sutils
from appy.ui.layout import Layouts, Layout
from appy.pod.xhtml2odt import XhtmlPreprocessor

#  - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
bn = '\n'

#  - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
class AutoCorrect:
    '''Defines the set of automatic corrections that will occur as you type in a
       poor field.'''

    # Standard replacements: chars being prefixed with a nbsp
    standard = {}

    # Chars that must be prefixed with a non-breakable space
    nbPrefixed = (':', ';', '!', '?', '%')
    for char in nbPrefixed:
        standard[char] = [('text', f' {char}')]

    # Replace double quotes by "guillemets" (angle quotes)
    quotes = {'"': {'if':'blankBefore',
                    1: [('text', '« ​')],
                    0: [('text', ' »')]}}

    def __init__(self, standard=True, quotes=True):
        '''Produces a specific auto-correct configuration'''
        r = {}
        if standard: r.update(AutoCorrect.standard)
        if quotes:   r.update(AutoCorrect.quotes)
        self.chars = r

    def inJs(self, toolbarId):
        '''Get the JS code allowing to define p_self.chars on the DOM node
           representing the poor toolbar.'''
        chars = sutils.getStringFrom(self.chars)
        return f"document.getElementById('{toolbarId}').autoCorrect={chars};"

# Default AutoCorrect configuration
AutoCorrect.default = AutoCorrect()

#  - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
class Icon:
    '''An icon from the toolbar'''

    def __init__(self, name, type, label=None, icon=None, data=None, args=None,
                 shortcut=None):
        # A short, unique name for the icon
        self.name = name
        # The following type of icons exist. Depending on the type, p_data
        # carries a specific type of information.
        #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
        # p_type     | p_data
        #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
        # "wrapper"  | the icon corresponds to a portion of text that will be
        #            | wrapped around some tag, using browser function
        #            | document.execCommand. p_data contains the command to pass
        #            | to this function.
        #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
        # "char"     | the icon corresponds to a char to insert into the field.
        #            | p_data is the char to insert.
        #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
        # "action"   | the icon corresponds to some action that is not
        #            | necessarily related to the field content. In that case,
        #            | p_data may be None or its semantics may be specific to
        #            | the action.
        #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
        # "dropdown" | a click on the icon will display a dropdown menu. In that
        #            | case, p_data may hold:
        #            | (a) a name starting with "js:". In that case, the
        #            |     remaining of the name must correspond to a Javascript
        #            |     function that will fill and manage the dropdown zone.
        #            |     Such JS functions will mainly be used by Appy itself.
        #            |     For example, the "smiley" icon uses this mechanism ;
        #            | (b) an unprefixed name. In that case, it must correspond
        #            |     to the name of a Python method being defined on the
        #            |     class where the current poor field is defined. This
        #            |     method will be called without arg and must return a
        #            |     list of strings, that will be rendered as clickable
        #            |     links in the dropdown. A click on such link will have
        #            |     the effect of injecting the corresponding string in
        #            |     the poor field, where the cursor is currently set.
        #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
        self.type = type
        # The i18n label for the icon's tooltip. Should include the keyboard
        # shortcut when present. If None, defaults to "icon_<name>"
        self.label = label or f'icon_{name}'
        # The name of the icon image on disk. If None, will be computed as
        # "icon_<name>.png".
        self.icon = icon or f'icon_{name}'
        # The data related to this icon, as described hereabove
        self.data = data
        # If p_data refers to a command, its optional args may be defined in
        # p_args.
        self.args = args
        # If a keyboard shortcut is tied to the icon, its key code is defined
        # here, as an integer. See JavasScript keycodes, https://keycode.info.
        self.shortcut = shortcut
        # Precompute this boolean
        self.dropdown = type == 'dropdown'

    def asDropdown(self, r, o):
        '''For an icon of type "dropdown", wraps the icon into a div allowing
           to hook the dropdown.'''
        data = self.data
        entries = []
        if data.startswith('js:'):
            # Entries will be added and managed by the JS function specified in
            # p_data. The specified JS function will be executed on when the
            # mouse hovers over the icon.
            overFun = f';{data[3:]}(this)'
        else:
            overFun = ''
            # A Python method. Call it to get the strings to inject in the
            # dropdown
            for entry in getattr(o, data)():
                if not isinstance(entry, str):
                    # We have an additional, custom info to add besides the
                    # string itself.
                    entry, info = entry
                else:
                    info = ''
                truncated = Px.truncateValue(entry, width=65)
                div = f'<div class="ddString"><a class="clickable" ' \
                      f'onmousedown="injectString(event)" ' \
                      f'title="{entry}">{truncated}</a>{info}</div>'
                entries.append(div)
            # Add a warning message if no string has been found
            if not entries:
                emptyText = o.translate('no_sentence')
                entries.append(f'<div class="legend">{emptyText}</div>')
        # Determine the dropdown width. It can be defined within p_self.args
        if self.args:
            width = self.args.split(',', 1)[0]
        else:
            # Set a default value
            width = '350px'
        return f'<div class="ddContainer" onmouseover="toggleDropdown(this)' \
               f'{overFun}" onmouseout="toggleDropdown(this,\'none\')">{r}' \
               f'<div class="dropdown" style="display:none;width:{width}">' \
               f'{bn.join(entries)}</div></div>'

    def get(self, o):
        '''Returns the HTML chunk representing this icon'''
        shortcut = str(self.shortcut) if self.shortcut else ''
        # Use event "mousedown" and not "onclick". That way, focus is kept on
        # the current poor. Else, if focus must be forced back to the poor, the
        # current position within it will be lost.
        onclick = 'onmousedown' if self.dropdown else 'onclick'
        iconUrl = o.buildUrl(self.icon)
        tooltip = o.translate(self.label)
        data = self.data or ''
        args = self.args or ''
        r = f'<img class="iconTB" src="{iconUrl}" title="{tooltip}" ' \
            f'name="{self.name}" onmouseover="switchIconBack(this,true)"' \
            f' onmouseout="switchIconBack(this,false)"' \
            f' data-type="{self.type}" data-data="{data}" data-args="{args}"' \
            f' data-shortcut="{shortcut}" {onclick}="useIcon(this)"/>'
        # Add specific stuff for a dropdown
        if self.dropdown: r = self.asDropdown(r, o)
        return r

# All available icons
Icon.all = [
  # Insert a smiley. 1st arg is the dropdown width. Following args are ranges of
  # decimal codes representing Unicode.
  # smileys or other symbols.
  # (a) 1st range are smileys
  # (b) 2nd range are dingbats
  # (c) 3rd range are transport-related icons
  Icon('smiley',    'dropdown', data='js:initSmileys',
       args='17em,128513-128591,9986-10160,128640-128704'),

  # Classical icons: bold, italic
  Icon('bold',      'wrapper',  data='bold', shortcut=66),
  Icon('italic',    'wrapper',  data='italic', shortcut=73),

  # Highlight the selected zone by setting a yellow background color
  Icon('highlight', 'wrapper',  data='hiliteColor', args='yellow', shortcut=72),

  # Remove any formatting from the selected zone
  Icon('unformat',  'wrapper',  data='removeFormat', shortcut=77),

  # Insert a non-breaking space (+ a zero-width space). If a zero-width space is
  # not inserted after the non-breaking one, Firefox converts them into standard
  # spaces everytime a char is encoded after a non-breaking space.
  Icon('blank',     'char',     data=' ​', shortcut=32),

  # Insert a non breaking dash
  Icon('dash',      'char',     data='‑', shortcut=54),

  # Insert a bulleted list
  Icon('bulleted',  'wrapper',  data='insertUnorderedList'),

  # Put the selected text in superscript or subscript
  Icon('sub',       'wrapper',  data='subscript'),
  Icon('sup',       'wrapper',  data='superscript'),

  # Duplicate selected text (not yet)
  #Icon('dup',       'action' , data='', shortcut=68),

  # Increment the field height by <data>%
  Icon('lengthen',  'action',  data='30', shortcut=56)
]

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
class Poor(Rich):
    '''Field allowing to encode XHTML text'''

    # Make some classes available here
    Icon = Icon
    AutoCorrect = AutoCorrect

    class Layouts(Rich.Layouts):
        '''Rich-specific layouts'''
        editBase = 'd2-f;rv='
        viewBase = 'fl'
        g = Layouts(edit=Layout(editBase, width=None),
                    view=Layout(viewBase, width=None))
        # A wide variant
        gw = Layouts(edit=Layout(editBase), view=Layout(viewBase))

    # Unilingual view
    viewUni = cellUni = Px('''<div style=":field.getWidgetStyle(False)"
     class=":field.getAttribute(o, 'viewCss')">::field.getInlineEditableValue(o,
       value or '-', layout, name=name, language=lg)</div>''')

    # The toolbar
    pxToolbar = Px('''
     <x var="tbId=tbid|field.name + '_tb'">
      <div class="toolbar" id=":tbId">
       <x for="icon in field.Icon.all">::icon.get(o)</x>
       <!-- Add inline-edition icons when relevant -->
       <x if="hostLayout">:field.pxInlineActions</x>
      </div>
      <!-- Configure auto-correct -->
      <script if="field.autoCorrect">::field.autoCorrect.inJs(tbId)</script>
     </x> ''',

     css = '''
      .toolbar { display:flex; height:24px; margin:2px 0 }
      .ddContainer { position: relative; display: inline }
      .ddString { padding: 3px 0 }
      .iconTB { padding: 3px; border-width: 1px; border: 1px transparent solid }
      .iconTBSel { background-color: #dbdbdb; border-color: #909090 }
      .smileyRange { display:flex; gap:1em; border-bottom: 1px solid lightgrey;
                     padding-bottom:0.5em; margin-bottom:0.5em; font-size:120% }
      .smileys { display:flex; gap:0.5em; flex-wrap:wrap; font-size:120% }
     ''',

     js='''
      const delCodes=[8,46];
      class Surgeon {
        // Performs various DOM triturations

        static wrapNodes(nodes) {
          // Wrap this array of p_nodes into a "div" tag
          let r = document.createElement('div');
          for (const node of nodes) r.appendChild(node);
          return r;
        }

        static isRoot(div) {
          // Return True if p_div is the root poor div
          return div.getAttribute('contenteditable') === 'true';
        }

        static cutAt(range) {
          // Cut and return the tail of the current selection
          let current = range.startContainer, r=[];
          if (current.nodeType == Node.TEXT_NODE) {
            // Cut a TextNode in 2 pieces
            let i = range.startOffset,
                tail = current.data.substring(i);
            if (tail) {
              r.push(document.createTextNode(tail));
              current.data = current.data.substring(0, i);
            }
            current = current.parentNode;
          }
          else {
            // Cut a container tag whose child nodes are probably TextNodes
            let children = current.childNodes,
                i = children.length - 1,
                j = range.startOffset, child;
            while (i >= j) {
              child = current.removeChild(children[i]);
              if (child.data) r.unshift(child);
              i = i-1;
            }
          }
          // Position the cursor after the cut element
          range.setStartAfter(current);
          range.collapse(true);
          return r;
        }

        static insertAt(sel, range, node, moveAfter) {
          /* Inserts p_node at the position indicated by p_range. If p_moveAfter
             is true, the cursor is moved to the end of the inserted node. */
          range.insertNode(node);
          if (moveAfter) range.setStartAfter(node);
          // Reinitialise the range
          range.collapse(true);
          sel.removeAllRanges();
          sel.addRange(range);
        }

        static cleanSel() {
          // Clean the text being currently selected within a poor
          let range = window.getSelection().getRangeAt(0);
          if (!range.collapsed) range.deleteContents();
        }

        static inject(type, content, outer) {
          /* Inject, within the currently selected poor, an element of this
             p_type, with this p_content. Inject it where the cursor is
             currently positioned. If text is selected, it is removed. If
             p_outer is true, one or several paragraphs are inserted. */
          let sel = window.getSelection(),
              range = sel.getRangeAt(0),
              many = false, node;
          // Delete the currently selected text, if any
          if (!range.collapsed) range.deleteContents();
          // Create, when relevant, the element to insert
          if (type == 'text') { // Insert string p_content as a TextNode
            node = document.createTextNode(content);
          }
          else if (type == 'node') { // Insert the node passed in p_content
            node = content;
          }
          else if (type == 'array') { // Insert p_content = an array of nodes
            node = content;
            many = true;
          }
          else { // Create the node named p_type, with this p_content
            node = document.createElement(type);
            node.appendChild(document.createTextNode(content));
          }
          // Insert the element(s)
          node = (many)? node : [node];
          let first = true, paraTail;
          for (const nod of node) {
            if (first) {
              if (outer) {
                /* Cut the remaining of the current paragraph: it will be
                   reinserted after all nodes will have been inserted. */
                paraTail = Surgeon.cutAt(range);
              }
              first = false;
            }
            Surgeon.insertAt(sel, range, nod, true);
          }
          // Reinsert v_paraTail if present
          if (paraTail && paraTail.length > 0) {
            Surgeon.insertAt(sel, range, Surgeon.wrapNodes(paraTail), false);
          }
        }
      }

      getIconsMapping = function(toolbar) {
        // Gets a mapping containing toolbar icons, keyed by their shortcut
        var r = {}, icons=toolbar.getElementsByClassName('iconTB'), key;
        for (const icon of icons) {
          key = icon.dataset.shortcut;
          if (key) r[parseInt(key)] = icon;
        }
        return r;
      }

      linkToolbar = function(toolbarId, target) {
        // Link the toolbar with its target div
        if (!target) {
          // Get the target div if not given in p_target
          target = document.getElementById(`${_rsplit(toolbarId, '_', 2)[0]}P`);
        }
        let toolbar = document.getElementById(toolbarId);
        toolbar['target'] = target;
        target['toolbar'] = toolbar;
        target['icons'] = getIconsMapping(toolbar);
      }

      switchIconBack = function(icon, selected) {
        icon.className = (selected)? 'iconTB iconTBSel': 'iconTB';
      }

      lengthenDiv = function(div, percentage) {
        // Lengthen this p_div by some p_percentage
        let rate = 1 + (percentage / 100);
            [height, unit] = splitUnit(div.style.minHeight);
        // Apply the rate
        height = Math.ceil(height * rate);
        // Reinject the new height to the correct area property
        div.style.minHeight = `${height.toFixed(2)}${unit}`;
      }

      duplicateSelection = function(div) {
        // Duplicates text selected in p_div
        let sel = window.getSelection(),
            range = sel.getRangeAt(0);
        // Do nothing if no text is selected
        if (range.collapsed) return;
        // To continue
      }

      useIcon = function(icon) {
        // Get the linked div (if already linked)
        let div = icon.parentNode['target'];
        if (!div) return;
        div.focus();
        let set=icon.dataset,
            type=set.type,
            data=set.data,
            args=set.args || null;
        if (type == 'wrapper') {
          // Wrap the selected text via the command specified in v_data
          document.execCommand(data, false, args);
        }
        else if (type == 'char') {
          // Insert a (sequence of) char(s) into the text
          Surgeon.inject('text', data);
        }
        else if (type == 'action') {
          // Actions
          if (icon.name == 'lengthen') lengthenDiv(div, parseInt(data));
          else if (icon.name == 'dup') duplicateSelection(div);
        }
      }

      setCaret = function(div) {
        // Ensure the caret is correctly positioned before encoding text
        let sel = window.getSelection(),
            range = sel.getRangeAt(0),
            curr = range.startContainer;
        // If the current node is a text node, get the parent div
        curr = (curr.nodeType == Node.TEXT_NODE)? curr.parentNode: curr;
        if (sel.isCollapsed && curr == div) {
          /* Structural problem: an empty para must be created and the caret
             must be positioned inside it. As a preamble, remove any silly br
             that would be present. */
          let child;
          for (let i=div.childNodes.length-1; i>=0; i--) {
            child = div.childNodes[i];
            if (child.tagName === 'BR') div.removeChild(child);
          }
          // Get existing content if any
          let existing = div.innerText || '';
          if (existing) div.innerText = '';
          let para = document.createElement('div'),
              text = para.appendChild(document.createTextNode(existing));
          div.appendChild(para);
          range.setStart(text, text.length);
          range.collapse(true);
          sel.removeAllRanges();
          sel.addRange(range);
        }
      }

      blankBefore = function(div) {
        /* Returns true if there is a blank (or nothing) before the currently
           selected char within p_div. */
        const sel = window.getSelection(),
              range = sel.getRangeAt(0),
              offset = range.startOffset;
        if (offset == 0) return true;
        let container = range.startContainer, prev;
        if (container.nodeType == Node.TEXT_NODE) {
          prev = container.textContent[offset-1];
        }
        else {
          prev = container.childNodes[offset-1].data.slice(-1);
        }
        return (prev === ' ') || (prev === ' '); // Breaking and non-breaking
      }

      applyAutoCorrect = function(div, nodes) {
        /* Apply an auto-correction by injecting these p_nodes into p_div, at
           the current cursor position. */
        if ('if' in nodes) {
          // The replacement to choose depends on a condition
          let condition = eval(nodes['if'])(div),
              key = (condition)? 1: 0;
          applyAutoCorrect(div, nodes[key]);
        }
        else {
          for (const node of nodes) Surgeon.inject(node[0], node[1]);
        }
      }

      // Triggered when the user hits a key in a poor
      onPoorKeyDown = function(event) {
        let div = event.target;
        if (event.ctrlKey || event.metaKey ||
            (event.altKey && event.keyCode == 32)) {
          /* Manage keyboard shortcuts. Key "alt" is allowed as alternative to
             "ctrl" when hitting "space" (32) (for Mac users), while key "meta"
             seems to be a replacement for "ctrl" on Mac for some shortcuts like
             cut and paste. */
          if (event.keyCode in div['icons']) {
            // Perform the icon's action
            setCaret(div);
            useIcon(div['icons'][event.keyCode]);
            event.preventDefault();
          }
        }
        else if (!delCodes.includes(event.keyCode)) {
          setCaret(div);
          // Perform auto-correction when relevant
          let autoCorrect = div['toolbar'].autoCorrect;
          if (autoCorrect && event.key in autoCorrect) {
            // Insert the replacement nodes instead of this char
            applyAutoCorrect(div, autoCorrect[event.key]);
            event.preventDefault();
          }
        }
      }

      injectString = function(event) {
        let tag = event.target;
        // Close the dropdown
        let dropdown = tag;
        while (!dropdown.classList.contains('dropdown')) {
          dropdown = dropdown.parentNode;
        }
        dropdown.style.display = 'none';
        // Find the corresponding poor
        let div = dropdown.parentNode.parentNode['target'];
        if (!div) return;
        div.focus();
        // Inject the sentence in it
        Surgeon.inject('text', tag.title);
        event.preventDefault();
      }

      renderSmileys = function(node, range) {
        /* Computes a chunk of XHTML containing all smileys from a given range.
           (a) If p_node is passed, it is the button used to display a given
               range of smileys. In that case, p_range is null: range info is
               stored on the node itself, and the smileys are injected in the
               node hosting smileys.
           (b) If p_range is passed, p_div is null: the function simply computes
               and returns the corresponding smileys.
        */
        if (!range) range = node.dataset.range;
        let [start, end] = range.split('-');
        start = parseInt(start);
        end = parseInt(end);
        let i = start, r = [];
        while (i <= end) {
          symbol = `&#${i};`;
          smiley = `<div class="clickable" title="${symbol}" \
                     onmousedown="injectString(event)">${symbol}</div>`;
          r.push(smiley);
          i += 1;
        }
        r = r.join('');
        if (node) {
          node.parentNode.nextElementSibling.innerHTML = r;
        }
        else return r;
      }

      initSmileys = function(div) {
        const icon = div.firstChild, dropdown = icon.nextElementSibling;
        // Do nothing if the dropdown has already been initialized
        if (dropdown.innerHTML) return;
        /* Create (a) a div with one icon per range, allowing to switch from one
           range to another, and (b) a div containing the smileys relative to
           the currently shown range, initialized with smileys from the first
           range. */
        let rangeIcons = [], ranges = icon.dataset.args.split(','),
            smileys, startR, iconR;
        // Remove the 1st element from v_ranges: it stores the dropdown width
        ranges.shift();
        for (const range of ranges) {
          startR = range.split('-')[0];
          iconR = `<div class="clickable" data-range="${range}" \
                        onclick="renderSmileys(this)">&#${startR};</div>`
          rangeIcons.push(iconR);
          if (!smileys) smileys = renderSmileys(null, range);
        }
        rangeIcons = rangeIcons.join('');
        dropdown.innerHTML = `<div class="smileyRange">${rangeIcons}</div> \
                              <div class="smileys">${smileys}</div>`;
      }

      // Insert pasted data into a poor field
      getPastedData = function(event) {
        // Prevent data to be directly injected
        event.stopPropagation();
        event.preventDefault();
        // Get pasted data via the clipboard API
        let clipboardData = event.clipboardData || window.clipboardData,
            pastedData = clipboardData.getData('text');
        if (!pastedData) return;
        // As a preamble, clean selected data
        Surgeon.cleanSel();
        // Split v_pastedData into paragraphs
        let paras = pastedData.split('\\n'),
            para = paras.shift();
        /* For the first paragraph, if we are at the root of the (empty)
           contenteditable zone, wrap it in a paragraph. Else, inject text in
           the current paragraph. */
        if (Surgeon.isRoot(event.target)) setCaret(event.target);
        document.execCommand('insertText', false, para);
        // Insert the next lines as "div" tags
        if (paras.length > 0) {
          for (let i=0; i < paras.length; i++) {
            if (!paras[i]) continue; // Ignore any empty content
            document.execCommand('insertParagraph', false);
            document.execCommand('insertText', false, paras[i]);
          }
        }
      }

      // Manipulates data copied within a poor field
      getCopiedData = function(event) {
        const sel = document.getSelection();
        event.clipboardData.setData('text/plain', sel.toString());
        event.preventDefault();
      }''')

    # Buttons for saving or canceling while inline-editing the field, rendered
    # within its toolbar.

    pxInlineActions = Px('''
      <div var="inToolbar=showToolbar and hostLayout;
                fdir='row' if inToolbar else 'column'"
           style=":f'display:flex;flex-direction:{fdir}'">
       <div>
        <img id=":f'{pid}_save'" src=":svg('saveS')"
             class=":'iconS %s' % ('clickable' if inToolbar else 'inlineIcon')"
             title=":_('object_save')"/></div>
       <div>
        <img id=":f'{pid}_cancel'" src=":svg('cancelS')"
             class=":'iconS %s' % ('clickable' if inToolbar else 'inlineIcon')"
             title=":_('object_cancel')"/></div>
      </div>
      <script>:'prepareForAjaxSave(%s,%s,%s,%s)' % \
               (q(name), q(o.iid), q(o.url), q(hostLayout))</script>''')

    # Unilingual edit
    editUni = Px('''
     <x var="pid=f'{name}_{lg}' if lg else name;
             tbid=f'{pid}_tb';
             x=hostLayout and o.Lock.set(o, field=field);
             showToolbar=field.showToolbar(ignoreInner=hostLayout);
             linkNow=hostLayout or not field.isInner();
             linkJs=field.linkToolbarJs(pid, lg, hostLayout, linkNow)">

      <!-- Show the toolbar when relevant -->
      <x if="showToolbar">:field.pxToolbar</x>

      <!-- Add buttons for inline-edition when relevant -->
      <x if="not showToolbar and hostLayout">:field.pxInlineActions</x>

      <!-- The poor zone in itself -->
      <div contenteditable="true" class="xhtmlE"
           style=":field.getWidgetStyle(True)"
           onfocus=":'' if linkNow else linkJs"
           onpaste="getPastedData(event)" oncopy="getCopiedData(event)"
           onkeydown="onPoorKeyDown(event)"
           id=":f'{pid}P'">::field.getInputValue(inRequest, requestValue,
                                                 value)</div>
      <!-- The hidden form field -->
      <textarea id=":pid" name=":pid" style="display:none"></textarea>

      <!-- Directly link the toolbar to the field when appropriate -->
      <script if="linkNow">:linkJs</script>
     </x>''')

    def __init__(self, validator=None, multiplicity=(0,1), default=None,
      defaultOnEdit=None, show=True, renderable=None, page='main', group=None,
      layouts=None, move=0, indexed=False, mustIndex=True, indexValue=None,
      searchable=False, filterField=None, readPermission='read',
      writePermission='write', width='25em', height='7em', maxChars=None,
      colspan=1, master=None, masterValue=None, focus=False, historized=False,
      mapping=None, generateLabel=None, label=None, sdefault='', scolspan=1,
      swidth=None, fwidth=10, sheight=None, persist=True, documents=False,
      languages=('en',), languagesLayouts=None, viewSingle=False,
      inlineEdit=False, view=None, cell=None, buttons=None, edit=None,
      custom=None, xml=None, translations=None, inject=False, valueIfEmpty='',
      viewCss='xhtmlV', autoCorrect=AutoCorrect.default, font=None,
      transformText=None, toItalicize=None):
        # Call the base constructor
        super().__init__(validator, multiplicity, default, defaultOnEdit,
          show, renderable, page, group, layouts, move, indexed, mustIndex,
          indexValue, searchable, filterField, readPermission, writePermission,
          width, height, maxChars, colspan, master, masterValue, focus,
          historized, mapping, generateLabel, label, sdefault, scolspan, swidth,
          fwidth, sheight, persist, None, None, documents, None,
          languages, languagesLayouts, viewSingle, inlineEdit, 'Standard',
          view, cell, buttons, edit, custom, xml, translations, inject,
          valueIfEmpty, viewCss, None, transformText, toItalicize)
        # As-you-type replacements are defined by placing an Autocorrect object
        # in this attribute.
        self.autoCorrect = autoCorrect
        # If you want to use a specific font shipped with Appy, set its name in
        # attribute "font". Currently, there is only a single font being
        # available:
        #                          NimbusSans-NBV
        #
        # It is a variant of the open soure font "Nimbus Sans", but whose
        # *N*on-*B*reaking chars are made *V*isible, the same way they are in
        # word processors, when mode "Show formatting marks" is enabled.
        #
        # WARNING
        #
        # In order to be loaded by the browser, the font as defined here must
        # also be defined in the UI config, within list config.ui.customFonts.
        self.font = font

    # Do not load ckeditor
    def getJs(self, o, layout, r, config): return

    def getWidgetStyle(self, edit):
        '''Returns style for the main poor tag'''
        # Potentially use a specific font shipped with Appy
        font = f'font-family:"{self.font}",sans-serif' if self.font else None
        if edit:
            r = f'width:{self.width};min-height:{self.height}'
            if font:
                r = f'{r};{font}'
        else:
            r = font if font else ''
        return r

    def linkToolbarJs(self, pid, lg, hostLayout, linkNow):
        '''Returns the Javascript code to execute for linking the toolbar to a
           given poor widget (several widgets may be there if p_self is an
           inner field).'''
        if hostLayout:
            # We are inline-editing the (sub-)field: it has its own toolbar
            id = pid
        else:
            # For inner fields, there is a unique global toolbar
            id = f'{self.name}_{lg}' if lg else self.name
        # When directly called when p_self is rendered, the current tag is a
        # script, not being passed in the "this" JS variable: it is useless to
        # mention it as parameter.
        lastParam = '' if linkNow else ', this'
        return f"linkToolbar('{id}_tb'{lastParam})"

    def getListHeader(self, c):
        '''When used as an inner field, the toolbar must be rendered only once,
           within the container field's header row corresponding to this
           field.'''
        # Inject the toolbar when appropriate
        if c.layout == 'edit' and self.showToolbar(ignoreInner=True):
            bar = self.pxToolbar(c)
        else:
            bar = ''
        header = super().getListHeader(c)
        return f'{header}{bar}'

    def showToolbar(self, ignoreInner=False):
        '''Show the toolbar if the field is not inner. Indeed, in that latter
           case, the toolbar has already been rendered in the container field's
           headers.'''
        # Do not show the toolbar if the field is an inner field, provided this
        # check must be performed.
        return True if ignoreInner else not self.isInner()

    def getXhtmlCleaner(self, o, forValidation=False):
        '''Returns a Cleaner instance tailored to p_self'''
        # More strict cleaning than the Rich
        tagsToIgnore = Cleaner.tagsToIgnoreWithContentStrict
        if forValidation:
            transform = italicize = None
        else:
            transform = self.transformText
            it = self.toItalicize
            italicize = self.getItalicized(o)
        return Cleaner(attrsToAdd=Cleaner.attrsToAddStrict,
                       propertiesToKeep=Cleaner.propertiesToKeepStrict,
                       tagsToIgnoreWithContent=tagsToIgnore, repair=True,
                       transformText=transform, toItalicize=italicize, logger=o)

    def validateUniValue(self, o, value):
        '''As a preamble, ensure p_value is XHTML'''
        value = XhtmlPreprocessor.preprocess(value, html=True, pre=False,
                                             paraTag='div')
        return super().validateUniValue(o, value)

    def getUniStorableValue(self, o, value, wrap=False):
        '''Gets the p_value as can be stored in the database within p_o'''
        if not value or value == '<br>': return
        # Ensure p_value is XHTML
        value = XhtmlPreprocessor.preprocess(value, html=True, pre=False,
                                             root='x', paraTag='div')
        return super().getUniStorableValue(o, value, wrap=wrap)

    def isInnerable(self):
        '''Poor fields are innerable (but richs are not)'''
        return True
#  - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

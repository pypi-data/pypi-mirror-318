### The `webinteract` module for simple web interaction

See the blog post [Web page interaction in
Python](https://blog.pg12.org/web-page-interaction-in-python) for a
more complete documentation of the `webinteract` module, or at
[PyPi](https://pypi.org/project/webinteract/) for an up-to-date (but
not detailed) documentation generated from the source code of the
module.

To-do (planned):
 - Better error handling and improved error messages
 - Better support for data harvesting

### To install and use the module

This module implements a simplified web interaction class. It is
implemented using the `splinter` module (that is implemented using
the `selenium` module).

The easiest way to install this module is to use `pip`:

```bash
pip install webinteract
```

This `pip` command will install the module and a console script
`webinteract` to use the module as a program. If you execute
`webinteract` without a script as an argument, it will open a browser
window and present you a prompt in the terminal where you do web
interaction. Try either the `-h` argument to `webinteract` or type
`help` in the prompt.

The web interaction approach of this module is to use simple web
interaction scripts where each line is a web interaction action.  The
web intedraction class `WebInteraction` implements all the different
action types, and it is meant to be easily extendible. This is an
example of a small web interaction script (stored in a file
`"add-ts.wia"`):

```python
setvals(url="https://a.web.page/", account="an@email.address")
visit(url)
fill(account, "id", "loginForm:id")
fill(pw, "id", "loginForm:password")
click("id", "loginForm:loginButton")
verify( \
  is_text_present("Login succeeded", wait_time=19), True, \
  "The text 'Login succeeded' is not present")
fill(date, "id", "registerForm:timeStamp")
click("id", "registerForm:addTS")
verify( \
  is_text_present("Register time stamp failed"), False, \
  "The text 'Register time stamp failed' is present")
```

The first we can observe is that the first line gives vaules to two
variables, `url` and `account`. If we look closer at the script, we
see a few other varibles also used in the script (`pw` and
`date`). They have to be added to the name space of the script with
the `update` method before the script is executed.  Each action type
and its usage is documented in its implementation the the
`WebInteraction` class (the methods at the end of the class
implementation decorated with the `webaction` decorator).

To perform the small web interaction script above we can do this (in
Python):

```python
# Import modules used in the example
from datetime import datetime
import webinteract                      # This module

# Create a time stamp (an example variable used it the script)
ts = datetime.timestamp(datetime.now())

# Open browser
web = webinteract.WebInteraction(driver_name="chrome")

# Add `pw` and `date` to the name space of the script
web.update({"pw": "a s3cret p4ssw0rd", "date": ts})

# Perform web interaction actions (the script)
web(open("add-ts.wia"))
```

See at the end of this file for a comment documentating how to use
the module as a program executing web interaction action scripts
(wia scripts).

For more information, check out the following blog post:

  >[`https://blog.pg12.org/web-page-interaction-in-python`](https://blog.pg12.org/web-page-interaction-in-python)

To print this documentation and all available web actions use the
command line argument `--doc [ACTION]` (where the optional argument is
used to print the documentation of a specific web action):

```bash
webinteract --doc
```

All available web actions:

 - [`attach_file`](#attach_file)
 - [`element_attach_file`](#element_attach_file)
 - [`check`](#check)
 - [`element_check`](#element_check)
 - [`clear`](#clear)
 - [`element_clear`](#element_clear)
 - [`click`](#click)
 - [`element_click`](#element_click)
 - [`click_link`](#click_link)
 - [`element_click_link`](#element_click_link)
 - [`cond`](#cond)
 - [`element_cond`](#element_cond)
 - [`doall`](#doall)
 - [`element_doall`](#element_doall)
 - [`fill`](#fill)
 - [`element_fill`](#element_fill)
 - [`find`](#find)
 - [`find_in_element`](#find_in_element)
 - [`find_link`](#find_link)
 - [`get`](#get)
 - [`element_get`](#element_get)
 - [`get_text`](#get_text)
 - [`element_get_text`](#element_get_text)
 - [`get_value`](#get_value)
 - [`element_get_value`](#element_get_value)
 - [`is_checked`](#is_checked)
 - [`element_is_checked`](#element_is_checked)
 - [`is_not_present`](#is_not_present)
 - [`is_present`](#is_present)
 - [`is_text_not_present`](#is_text_not_present)
 - [`is_text_present`](#is_text_present)
 - [`scroll_to`](#scroll_to)
 - [`element_scroll_to`](#element_scroll_to)
 - [`select`](#select)
 - [`element_select`](#element_select)
 - [`setvals`](#setvals)
 - [`uncheck`](#uncheck)
 - [`element_uncheck`](#element_uncheck)
 - [`verify`](#verify)
 - [`visit`](#visit)
 - [`wait`](#wait)

### All `webinteract` web actions documented

#### <a id="attach_file"></a>`attach_file`

*Action `attach_file` attachs a file to a web element*

The signature of `attach_file`:

```python
attach_file(file_path: str, stype: SelectorType, sval: str, index: int | None = None)
```

Attach a file to a web element (a file input element).  In
this example, the file `"/path/to/file"` is attached to a web
element with the name `"thefile"`:

```python
attach_file("/path/to/file", "name", "thefile")
```

Arguments and return value of the action `attach_file`:

 - `file_path`: Absolute path to file.

 - `stype`: The selector type.

 - `sval`: The value of the selector type.

 - `index`: Choose from the list of matching elements (default `None`).

#### <a id="element_attach_file"></a>`element_attach_file`

*Action `element_attach_file` attachs a file to the web element*

The signature of `element_attach_file`:

```python
element_attach_file(element: splinter.element_list.ElementList, index: int | None = None)
```

Attach a file to the web element (a file input element).

Arguments and return value of the action `attach_file`:

 - `file_path`: Absolute path to file.

 - `element`: A list of the web elements.

 - `index`: Choose from the list of matching elements (default `None`).

#### <a id="check"></a>`check`

*Action `check` checks a web element (checkbox)*

The signature of `check`:

```python
check(stype: SelectorType, sval: str, index: int | None = None, doall: bool = False)
```

Check a checkbox web element matching the selector `stype`
with the value `sval`. This example checks the fourth checkbox
on the web page (with index 3):

```python
check("xpath", "//input[@type='checkbox']", 3)
```

Arguments and return value of the action `check`:

 - `stype`: The selector type.

 - `sval`: The value of the selector type.

 - `index`: Choose from the list of matching elements (default `None`).

 - `doall`: If index is `None` and this is `True`, the action is
performed on all matching web elements.

#### <a id="element_check"></a>`element_check`

*Action `element_check` checks the web element (checkbox)*

The signature of `element_check`:

```python
element_check(element: splinter.element_list.ElementList, index: int | None = None, doall: bool = False)
```

Check the checkbox web element.

Arguments and return value of the action `element_check`:

 - `element`:  A list of the web elements.

 - `index`: Choose from the list of elements (default `None`).

 - `doall`: If index is `None` and this is `True`, the action is
performed on all matching web elements.

#### <a id="clear"></a>`clear`

*Action `clear` clears a web element*

The signature of `clear`:

```python
clear(stype: SelectorType, sval: str, index: int | None = None, doall: bool = False)
```

Reset the field value of a web element matching the selector
`stype` with the value `sval`. This example clears a field
with the name `"search"`:

```python
clear("name", "search")
```

Arguments and return value of the action `clear`:

 - `stype`: The selector type.

 - `sval`: The value of the selector type.

 - `index`: Choose from the list of matching elements (default `None`).

 - `doall`: If index is `None` and this is `True`, the action is
performed on all matching web elements.

#### <a id="element_clear"></a>`element_clear`

*Action `element_clear` clears the web element*

The signature of `element_clear`:

```python
element_clear(element: splinter.element_list.ElementList, index: int | None = None, doall: bool = False)
```

Reset the field value of the web element.

Arguments and return value of the action `element_clear`:

 - `element`:  A list of the web elements.

 - `index`: Choose from the list of elements (default `None`).

 - `doall`: If index is `None` and this is `True`, the action is
performed on all matching web elements.

#### <a id="click"></a>`click`

*Action `click` clicks a web element (button)*

The signature of `click`:

```python
click(stype: SelectorType, sval: str, index: int | None = None)
```

Click on a web element matching the selector `stype` with the
value `sval`. This example clicks on a web element with the
text `"OK"` (typically a button):

```python
click("text", "OK")
```

Arguments and return value of the action `click`:

 - `stype`: The selector type.

 - `sval`: The value of the selector type.

 - `index`: Choose from the list of matching elements (default `None`).

#### <a id="element_click"></a>`element_click`

*Action `element_click` clicks the web element (button)*

The signature of `element_click`:

```python
element_click(element: splinter.element_list.ElementList, index: int | None = None)
```

Click on the web element.

Arguments and return value of the action `element_click`:

 - `element`: A list of the web elements.

 - `index`: Choose from the list of elements (default `None`).

#### <a id="click_link"></a>`click_link`

*Action `click_link` clicks a link*

The signature of `click_link`:

```python
click_link(ltype: LinkType, lval: str, index: int = 0)
```

Click on a link element matching the selector `ltype` with the
value `lval`. This example clicks on a link element with the
partial text `"news"`:

```python
click_link("partial_text", "news")
```

Arguments and return value of the action `click_link`:

 - `ltype`: The link selector type.

 - `lval`: The value of the link selector type.

 - `index`: Choose from the list of matching elements (default 0).

#### <a id="element_click_link"></a>`element_click_link`

*Action `element_click_link` clicks the link*

The signature of `element_click_link`:

```python
element_click_link(element: splinter.element_list.ElementList, index: int = 0)
```

Click on the link element.

Arguments and return value of the action `click_link`:

 - `element`: A list of the web elements.

 - `index`: Choose from the list of elements (default 0).

#### <a id="cond"></a>`cond`

*Do action a web element if condition is true*

The signature of `cond`:

```python
cond(condition: bool, stype: SelectorType, sval: str, ifaction: ActionFunc, *args: list, elseaction: ActionFunc = None, index: int = 0, **kw: dict) -> str | None
```

Do `ifaction` if condition is true. If provided, do elseaction
if condition is false.  This example unchecks the checkbox
element `checkbox1` if it is checked, and checks if it is
unchecked (a checkbox toggle):

```python
cond( \
  verify(element_get_value(checkbox1), "on", assert_it = False), \
  "name", "checkbox1", \
  ifaction = element_uncheck, elseaction = element_check)
```

Arguments and return value of the action `cond`:

 - `condition`: The condition.

 - `stype`: The selector type.

 - `sval`: The value of the selector type.

 - `ifaction`: The action performed if condition is true.

 - `args`: Arguments to the action (both `ifaction` and `elseaction`).

 - `elseaction`: The action performed if condition is false
(default `None`).

 - `index`: Choose from the list of matching elements (default 0).

 - `kw`: Keyword arguments to the action (both `ifaction` and
`elseaction`).

 - `return`: The aggregated result of all actions or None.

#### <a id="element_cond"></a>`element_cond`

*Do action on the web element if condition is true*

The signature of `element_cond`:

```python
element_cond(condition: bool, element: splinter.element_list.ElementList, ifaction: ActionFunc, *args: list, elseaction: ActionFunc = None, index: int = 0, **kw: dict) -> str | None
```

Do `ifaction` if condition is true. If provided, do elseaction
if condition is false.  This example unchecks the checkbox
element `checkbox1` if it is checked, and checks if it is
unchecked (a checkbox toggle):

```python
element_cond( \
  verify(element_get_value(checkbox1), "on", assert_it = False), \
  checkbox1, ifaction = element_uncheck, elseaction = element_check)
```

Arguments and return value of the action `element_cond`:

 - `condition`: The condition.

 - `element`: A list of the web elements.

 - `ifaction`: The action performed if condition is true.

 - `args`: Arguments to the action (both `ifaction` and `elseaction`).

 - `elseaction`: The action performed if condition is false
(default `None`).

 - `index`: Choose from the list of matching elements (default 0).

 - `kw`: Keyword arguments to the action (both `ifaction` and
`elseaction`).

 - `return`: The aggregated result of all actions or None.

#### <a id="doall"></a>`doall`

*Do action on all elements of list of web elements*

The signature of `doall`:

```python
doall(stype: SelectorType, sval: str, action: ActionFunc, *args: list, sep: str = '\n', **kw: dict) -> str | None
```

Do the same action on all web elements in the web element
list. In this example, the value of all select elements on a
web page are fetched:

```python
doall("tag", "select", element_get_value)
```

Arguments and return value of the action `doall`:

 - `stype`: The selector type.

 - `sval`: The value of the selector type.

 - `action`: The action performed on each element.

 - `args`: Arguments to the action.

 - `sep`: A separator inserted between each of result returned if
the action returns a result (default `"\n"`)

 - `kw`: Keyword arguments to the action.

 - `return`: The aggregated result of all actions or None.

#### <a id="element_doall"></a>`element_doall`

*Do action on all elements of list of the web elements*

The signature of `element_doall`:

```python
element_doall(elements: splinter.element_list.ElementList, action: ActionFunc, *args: list, sep: str = '\n', **kw: dict) -> str | None
```

Do the same action on all web elements in the web element
list. In this example, all chekboxes on a web page are
checked:

```python
element_doall( \
  find("xpath", "//input[@type='checkbox']"), element_check)
```

Arguments and return value of the action `element_doall`:

 - `elements`: A list of the web elements.

 - `action`: The action performed on each element.

 - `args`: Arguments to the action.

 - `kw`: Keyword arguments to the action.

 - `return`: The aggregated result of all actions or None.

#### <a id="fill"></a>`fill`

*Action `fill` fills the value in a web element*

The signature of `fill`:

```python
fill(val: str, stype: SelectorType, sval: str, index: int | None = None, doall: bool = False)
```

Fill in the value `val` in a web element matching the selector
`stype` with the value `sval`. In this example, a web element with
the name `"search"` is filled with the text `"Python"`:

```python
fill("Python", "name", "search")
```

Arguments and return value of the action `fill`:

 - `val`: The value to fill-in.

 - `stype`: The selector type.

 - `sval`: The value of the selector type.

 - `index`: Choose from the list of matching elements (default `None`).

 - `doall`: If index is `None` and this is `True`, the action is
performed on all matching web elements.

#### <a id="element_fill"></a>`element_fill`

*Action `element_fill` fills the value in the element*

The signature of `element_fill`:

```python
element_fill(val: str, element: splinter.element_list.ElementList, index: int | None = None, doall: bool = False)
```

Fill in the value `val` in the web element.

Arguments and return value of the action `element_fill`:

 - `val`: The value to fill-in.

 - `element`: A list of the web elements.

 - `index`: Choose from the list of elements (default `None`).

 - `doall`: If index is `None` and this is `True`, the action is
performed on all matching web elements.

#### <a id="find"></a>`find`

*Action `find` finds web elements on a web page*

The signature of `find`:

```python
find(stype: SelectorType, sval: str) -> splinter.element_list.ElementList
```

This action finds web elements based on a selector type and
the value of such a selector. This example returns a list of
web elements with the id `"filter"` (often a list with a single
element):

```python
find("id", "filter")
```

Another example using an XPath selector to find all `a`
(anchor) elements with an attribute `title` that has the value
`"log out"` (often a list with a single element):

```python
find("xpath", "//a[@title='log out']")
```

Arguments and return value of the action `find`:

 - `stype`: The selector type (either `"css"`, `"id"`, `"name"`,
`"tag"`, `"text"`, `"value"`, or `"xpath"`).

 - `sval`: The value of the selector type.

 - `return`: A list of the web elements matching the selector
`stype` with the value `sval`.

#### <a id="find_in_element"></a>`find_in_element`

*Action `find_in_element` finds web elements inside the web element*

The signature of `find_in_element`:

```python
find_in_element(stype: SelectorType, sval: str, element: splinter.element_list.ElementList, index: int = 0) -> splinter.element_list.ElementList
```

This action finds web elements based on a selector type and
the value of such a selector inside the given web
element. This example returns a list of web elements with the
name `"filter"` from inside a web element with the id
`"form"`:

```python
find_in_element("name", "filter", find("id", "form"), 0)
```

Arguments and return value of the action `find`:

 - `stype`: The selector type (either `"css"`, `"id"`, `"name"`,
`"tag"`, `"text"`, `"value"`, or `"xpath"`).

 - `sval`: The value of the selector type.

 - `element`: Find the web element inside one of these elements.

 - `index`: Choose from the list of elements (default 0).        

 - `return`: A list of the web elements matching the selector
`stype` with the value `sval`.

#### <a id="find_link"></a>`find_link`

*Action `find_link` finds link elements*

The signature of `find_link`:

```python
find_link(ltype: LinkType, lval: str) -> splinter.element_list.ElementList
```

The action `find_link` returns link web elements based on a
link selector type and the value of such a link selector. This
example returns a list of link elements with `href` attribute
values containing `"filter"`:

```python
find_link("partial_href", "filter")
```

Arguments and return value of the action `find_link`:

 - `ltype`: The link selector type.

 - `lval`: The value of the link selector type.

 - `return`: A list of matching link elements.

#### <a id="get"></a>`get`

*Action `get` gets the value or text of a web element*

The signature of `get`:

```python
get(stype: SelectorType, sval: str, index: int = 0) -> str
```

Get the value or text of a web element matching the selector
`stype` with the value `sval`. An example where we get the
value or text of an element with the id `"about"`:

```python
get("id", "about")
```

Arguments and return value of the action `get`:        

 - `stype`: The selector type.

 - `sval`: The value of the selector type.

 - `index`: Choose from the list of matching elements (default 0).

 - `return`: The value or text of a web element matching the
selector `stype` with the value `sval`.

#### <a id="element_get"></a>`element_get`

*Action `element_get` gets the value or text of the web element*

The signature of `element_get`:

```python
element_get(element: splinter.element_list.ElementList, index: int = 0) -> str
```

Get the value or text of the given web element.

Arguments and return value of the action `element_get`:        

 - `element`: A list of the web elements.

 - `index`: Choose from the list of matching elements (default 0).

 - `return`: The value or text of a web element.

#### <a id="get_text"></a>`get_text`

*Action `get_text` gets the text of a web element*

The signature of `get_text`:

```python
get_text(stype: SelectorType, sval: str, index: int = 0) -> str
```

Get the text of a web element matching the selector stype with
the value sval. An example where we get the text of the third
element (at index 2) with the tag `"h2"`:

```python
get_text("tag", "h2", 2)
```

Arguments and return value of the action `get_text`:

 - `stype`: The selector type.

 - `sval`: The value of the selector type.

 - `index`: Choose from the list of matching elements (default 0).

 - `return`: The text of a web elements matching the selector
`stype` with the value `sval`.

#### <a id="element_get_text"></a>`element_get_text`

*Action `element_get_text` gets the text of the web element*

The signature of `element_get_text`:

```python
element_get_text(element: splinter.element_list.ElementList, index: int = 0) -> str
```

Returns true if te web element is checked.

Arguments and return value of the action `element_get_text`:

 - `element`:  A list of the web elements.

 - `index`: Choose from the list of elements (default 0).

 - `return`: The text of the web element.

#### <a id="get_value"></a>`get_value`

*Create action `get_value` gets the value of a web element*

The signature of `get_value`:

```python
get_value(stype: SelectorType, sval: str, index: int = 0) -> str
```

Get the value of a web element matching the selector stype
with the value sval. An example where we get the value of an
element with the name `"aggregate"`:

```python
get_value("name", "aggregate")
```

Arguments and return value of the action `get_value`:

 - `stype`: The selector type.

 - `sval`: The value of the selector type.

 - `index`: Choose from the list of matching elements (default 0).

 - `return`: The value of a web elements matching the selector
`stype` with the value `sval`.

#### <a id="element_get_value"></a>`element_get_value`

*Action `element_get_value` gets the value of the web element*

The signature of `element_get_value`:

```python
element_get_value(element: splinter.element_list.ElementList, index: int = 0) -> str
```

Get the value of the web element.

Arguments and return value of the action `element_get_value`:

 - `element`: A list of the web elements.

 - `index`: Choose from the list of elements (default 0).

 - `return`: The value of the web element.

#### <a id="is_checked"></a>`is_checked`

*Create action `is_checked` checks if a web element is checked*

The signature of `is_checked`:

```python
is_checked(stype: SelectorType, sval: str, index: int = 0) -> str
```

Returns true if a web element matching the selector stype with
the value sval is checked. An example where we check
an element with the name `"checkbox1"`:

```python
is_checked("name", "checkbox1")
```

Arguments and return value of the action `is_checked`:

 - `stype`: The selector type.

 - `sval`: The value of the selector type.

 - `index`: Choose from the list of matching elements (default 0).

 - `return`: True if a web element (checkbox) matching the
selector `stype` with the value `sval` is checked.

#### <a id="element_is_checked"></a>`element_is_checked`

*Action `element_is_checked` checks if the web element is checked*

The signature of `element_is_checked`:

```python
element_is_checked(element: splinter.element_list.ElementList, index: int = 0) -> bool
```

Check if the web element (checkbox) is checked.

Arguments and return value of the action `element_is_checked`:

 - `element`: A list of the web elements.

 - `index`: Choose from the list of elements (default 0).

 - `return`: True if the web element (checkbox) is checked.

#### <a id="is_not_present"></a>`is_not_present`

*Action `is_not_present` checks if a web element is not present*

The signature of `is_not_present`:

```python
is_not_present(stype: SelectorType, sval: str, wait_time: int | None = None) -> bool
```

The action `is_not_present` checks if a web element based on
the selector type `stype` with the value `sval` is not
present. This example returns `True` if a web element with
name `"loginform"` is not present:

```python
is_not_present("name", "loginform")
```

Arguments and return value of the action `is_not_present`:

 - `stype`: The selector type.

 - `sval`: The value of the selector type.

 - `wait_time`: How long to wait for the web element to be
present (default `None`)

 - `return`: Returns True if the web element is not present.

#### <a id="is_present"></a>`is_present`

*Action `is_present` checks if a web element is present*

The signature of `is_present`:

```python
is_present(stype: SelectorType, sval: str, wait_time: int | None = None) -> bool
```

The action `is_present` checks if a web element based on a
selector type and the value of such a selector is present.
This example returns `True` if a web element with id `"news"`
is present:

```python
is_present("id", "news")
```

Arguments and return value of the action `is_present`:

 - `stype`: The selector type.

 - `sval`: The value of the selector type.

 - `wait_time`: How long to wait for the web element to be
present (default `None`).

 - `return`: Returns True if the web element is present.

#### <a id="is_text_not_present"></a>`is_text_not_present`

*Action `is_text_present` checks if a text is not present*

The signature of `is_text_not_present`:

```python
is_text_not_present(text: str, wait_time: int | None = None) -> bool
```

The action `is_text_not_present` checks if the text is not
present. This example returns `True` if the text `"Login
failed"` is not present:

```python
is_text_not_present("Login failed")
```

Arguments and return value of the action `is_text_not_present`:

 - `text`: The text that should't be present.

 - `wait_time`: How long to wait for the text to be present
(default `None`).

 - `return`: Returns `True` if the text is not present.

#### <a id="is_text_present"></a>`is_text_present`

*Action `is_text_present` checks if a text is present*

The signature of `is_text_present`:

```python
is_text_present(text: str, wait_time: int | None = None) -> bool
```

The action `is_text_present` checks if the text is
present. This example returns `True` if the text `"Login
succeeded"` is present within 3 seconds:

```python
is_text_present("Login succeeded", 3)
```

Arguments and return value of the action `is_text_present`:

 - `text`: The text to find.

 - `wait_time`: How long to wait for the text to be present
(default `None`).

 - `return`: Returns `True` if the text is present.

#### <a id="scroll_to"></a>`scroll_to`

*Action `scroll_to` scrolls to a web element*

The signature of `scroll_to`:

```python
scroll_to(stype: SelectorType, sval: str, index: int | None = None)
```

Scroll to a web element matching the selector `stype` with the
value `sval`. In this example, the view is scrolled to a `div`
element with a `class` attribute having the value
`"signature"`:

```python
scroll_to("xpath", "//div[@class='signature']")
```

Arguments and return value of the action `scroll_to`:

 - `stype`: The selector type.

 - `sval`: The value of the selector type.

 - `index`: Choose from the list of matching elements (default `None`).

#### <a id="element_scroll_to"></a>`element_scroll_to`

*Action `element_scroll_to` scrolls to the web element*

The signature of `element_scroll_to`:

```python
element_scroll_to(element: splinter.element_list.ElementList, index: int | None = None)
```

Scroll to the web element.

Arguments and return value of the action `element_scroll_to`:

 - `element`: A list of the web elements.

 - `index`: Choose from the list of elements (default `None`).

#### <a id="select"></a>`select`

*Action `select` selects the value in a web element*

The signature of `select`:

```python
select(val: str, stype: SelectorType, sval: str, index: int | None = None, doall: bool = False)
```

Select the given value `val` in a select web element matching
the selector `stype` with the value `sval`. In this example,
`"year"` is selected in the web element with the name
`"type"`:

```python
select("year", "name", "type")
```

Arguments and return value of the action `select`:

 - `val`: The value to fill in.

 - `stype`: The selector type.

 - `sval`: The value of the selector type.

 - `index`: Choose from the list of matching elements (default `None`).

 - `doall`: If index is `None` and this is `True`, the action is
performed on all matching web elements.

#### <a id="element_select"></a>`element_select`

*Action `element_select` selects the value in the web element*

The signature of `element_select`:

```python
element_select(val: str, element: splinter.element_list.ElementList, index: int | None = None, doall: bool = False)
```

Select the given value `val` in the select web the element.

Arguments and return value of the action `element_select`:

 - `val`: The value to fill in.

 - `element`: A list of the web elements.

 - `index`: Choose from the list of elements (default `None`).

 - `doall`: If index is `None` and this is `True`, the action is
performed on all matching web elements.

#### <a id="setvals"></a>`setvals`

*Action `setvals` sets values used later in the script*

The signature of `setvals`:

```python
setvals(**kw)
```

The `setvals` action can be used to give a value to one or more
variables used later in the script.  This example sets the
values of the two variables `url` and `email`:

```python
setvals(url = "https://a.web.page/", email = "an@email.address")
```

The variables `url` and `email` can then be used in other
actions later in the script. `setvals` updates the name space
of the script with the varibales with the given value.

It is also possible to use web actions that returns a value
with `setvals`. In this example we set the value of the
variable `tag` to the value of an element with an id `"tag"`:

```python
setvals(tag = get_value("id", "tag"))
```

Arguments and return value of the action `setvals`:

 - `kw`: Named arguments that set values in the namespace.

#### <a id="uncheck"></a>`uncheck`

*Action `uncheck` unchecks a web element (checkbox)*

The signature of `uncheck`:

```python
uncheck(stype: SelectorType, sval: str, index: int | None = None, doall: bool = False)
```

Uncheck a checkbox web element matching the selector `stype`
with the value `sval`. This example unchecks a checkbox with
id `"include-comments"`:

```python
uncheck("id", "include-comments")
```

Arguments and return value of the action `uncheck`:

 - `stype`: The selector type.

 - `sval`: The value of the selector type.

 - `index`: Choose from the list of matching elements (default `None`).

 - `doall`: If index is `None` and this is `True`, the action is
performed on all matching web elements.

#### <a id="element_uncheck"></a>`element_uncheck`

*Action `element_uncheck` unchecks the web element (checkbox)*

The signature of `element_uncheck`:

```python
element_uncheck(element: splinter.element_list.ElementList, index: int | None = None, doall: bool = False)
```

Uncheck the checkbox web element.

Arguments and return value of the action `element_uncheck`:

 - `element`:  A list of the web elements.

 - `index`: Choose from the list of elements (default `None`).

 - `doall`: If index is `None` and this is `True`, the action is
performed on all matching web elements.

#### <a id="verify"></a>`verify`

*Action `verify` checks that two values match*

The signature of `verify`:

```python
verify(val1: Any, val2: Any, errmsg: str = 'No match', assert_it: bool = True) -> bool | None
```

The created action checks that the two given value arguments
match.  If they don't match and the `assert_it` argument is
`True` (the default), the `WebInteractionError` is raised (the
wia-script terminates). If they don't match and the
`assert_it` argument is `False`, the action returns
`False`. Each value argument is either a value or an
action. If it is an action, the action is performed and the
result of the action is the value compared with the other
argument. Three examples:

```python
verify(url, "https://a.web.page/")
verify(is_present("id", "afilter"), True, "No filter")
verify("web", get("id", "searchtxt"), "Action fill failed")
```

The first example verifies that `url` has the value
`"https://a.web.page/"`. The second example verifies that a web
element with id `"afilter"` is present (`is_element_present`
returns `True`). The third example verifies that a web element
with id `"searchtxt"` has the value (or text) `"web"` (`get`
returns `"web"`).

The third optional argument is the error message given if the
verification fails and the `WebInteractionError` is
raised.

Arguments and return value of the action `verify`:

 - `val1`: Value one.

 - `val2`: Value two.

 - `errmsg`: The error message given if the verification fails
and the `WebInteractionError` is raised.

 - `assert_it`: Should the action raise the `WebInteractionError`
if the values don't match. The default is `True`.

 - `return`: `True` if the two values match, `False`
otherwise. If the `assert_it` argument is `True`, the
WebInteractionError exception is raised if the two values do
not match, and if they match, nothing is returned (and nothing
happens).

#### <a id="visit"></a>`visit`

*Action `visit` is used to open a web page (URL)*

The signature of `visit`:

```python
visit(url: str)
```

This action opens a web page (URL). The actions that follow
will interact with this web page:

```python
visit("https://a.web.page/")
```

Actions following this action operates on this web page. The
arguments to this action is the same as the `visit` method
from the `Browser` class in the `splinter` module
(https://splinter.readthedocs.io/en/latest/browser.html). To
be more presise, the returned method is the `visit` method
from the `Browser` class in the `splinter` module (and for moe
detailed documentation, please use the `splinter` module
documentation).

Arguments and return value of the action `visit`:

 - `url`: The URL to be visited.

#### <a id="wait"></a>`wait`

*Action `wait` waits for the given seconds in a script*

The signature of `wait`:

```python
wait(wait_time: int = 1)
```

Used if you need to wait for web elements to be loaded or when
debugging scripts. Some other actions, like `is_present`, can
also wait for a while if the expected element is not present
yet (they have an optional argument `wait_time`).

 - `wait_time`: The amount of time to wait in seconds (default 1).


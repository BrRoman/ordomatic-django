## Ordomatic

Ordomatic is a Django web application that creates customized Catholic liturgical calendars (called 'Ordo').


### Specifications
- Ordomatic allows the final user to manage the liturgical Ordo of his community, parish or diocese.
- Ordomatic is a web application, which have two benefits:
  1. It is multi-platform.
  2. The user (who will not necessarily be a hacker) hasn't anything to install on his computer, nor server nor database.
- Ordomatic will fit to every situation: either Ordinary or Extraordinary forms, customization and formatting of each day's header and body (see below), and so on.

---


### Main lines
The user gathers all the components of his Ordo into a database via the UI. Then he selects a year, and Ordomatic outputs the Ordo of this year, in one of the following formats:
  - Plain text: `Easter`
  - Markup-formatted text: `<h3>Easter</h3>`
  - LaTeX-formatted text: `\MyStyle{Easter}`
  - PDF

One user can create as many Ordos as he wants.

Each Ordo will contain:
- Days:
    * The days of the Temporal will stand around the Christmas' and Easter's dates (for example 'Christmas + 7' or 'Easter - 14').
    * The days of the Sanctoral days will of course have fixed date (for example '03-19').
    * Each Day will contain:
        - A strength, so that Ordomatic can determine, by comparison, which day (Temporal or Sanctoral) is celebrated at a given date.
        - A header and a body, which will be splitted into as many parts as the user wants. For example, the header can consist in many blocks, and the body can contain many lines.
        - Each one of these elements will have its own strength, so that it can appear in the final output, even if his parent (Temporal or Sanctoral day) is overriden by an other day. This should be sufficient to manage the Extraordinary form's commemorations.
- Snippets, i.e. some variable elements reusable anywhere in the days' headers or bodies.

---


### TODO
<span style="color: green;">✔</span> Starting Django application.

<span style="color: green;">✔</span> Main template.

◻ Routing and CRUD's pages for Users, Ordos, Days and Snippets.

<span style="color: green;">✔</span> Installing on [pythonanywhere.com](https://www.pythonanywhere.com/)

<span style="color: green;">✔</span> Models.

<span style="color: green;">✔</span> FIXME: installing mysqlclient.

◻ Authentication and security.

◻ Storing the Days of 2 basic Ordos (OF and EF) that will be duplicable by the user, so that he doesn't have to start from scratch when creating a new Ordo.

◻ Basic pdf with available Python modules.

◻ Advanced pdf with LaTeX: either installing LaTeX on [pythonanywhere.com](https://www.pythonanywhere.com/), or sending the user to [overleaf.com](https://www.overleaf.com/).
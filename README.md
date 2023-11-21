# Infinite scroll implementation
This is an implementation of infinite scroll, using the IntersectionObserver API
provided by most browsers. This is what allows us to detect when an infinite scroll
marker scrolls into the viewport, and subsequently carry out an AJAX request to the server
for more results. A FLASK web server is also provided, and implements a search endpoint to send
requests to. It just returns fake data for now, but it could easily be adapted to fetch results
from a database.

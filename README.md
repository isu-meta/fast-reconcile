# FAST-reconcile

An OpenRefine reconciliation service for [FAST](http://www.oclc.org/research/activities/fast.html?urlm=159754).

> FAST is available as Linked Data, which is an approach to publishing
> data which enhances the utility of information on the web by making
> references to persons, places, things, etc. more consistent and
> linkable across domains.

The service queries the [FAST AutoSuggest API](http://www.oclc.org/developer/documentation/fast-linked-data-api/request-types)
and provides normalized scores across queries for reconciling in Refine.

## Usage

Run locally as:
~~~~
$ python reconcile.py
~~~~
This will start the service on port 5000. The service can be accessed at 
http://0.0.0.0:5000/reconcile, http://localhost:5000/reconcile or
http://127.0.0.1:5000/reconcile.

If you want to run `fast-reconcile` on a different port, you can specify
the port number using the `-p` or `--port` flags like so:
~~~~
$ python reconcile.py -p 2000 
~~~~
or
~~~~
$ python reconcile.py --port 2000 
~~~~
This can be especially useful if you're running multiple local OpenRefine services.
To avoid conflicting with other network services that use reserved ports, use port
numbers higher than 1023.

If you'd like to run develop `fast-reconcile`, it can be helpful to use the `--debug`
flag:
~~~~
$ python reconcile.py --debug
~~~~

## License and provenance

This code is available under the terms of the [3-Clause BSD license](https://github.com/isu-meta/fast-reconcile/blob/master/LICENSE).

This is code is based on the [demo reconcilliation service](https://github.com/mikejs/reconcile-demo)
written by Michael Stephens. It has been forked from Christina Harlow's [Python 3 adaptation](https://github.com/cmharlow/fast-reconcile)
of Ted Lawless' original [fast-reconcile](https://github.com/lawlesst/fast-reconcile) service. 

=============
microsky
=============

A Bluesky client for Python and MicoroPython.

Usage
-----------------

See microsky.py and the Bluesky HTTP API reference https://docs.bsky.app/docs/category/http-reference for usage.

Install
-----------------

Python
+++++++++++++++

::

   pip install microsky

MicroPython
+++++++++++++++

Go interactive shell and install with mip as follow.
::

   >>> import mip
   >>> mip.install("urequests")
   >>> mip.install("https://github.com/nakagami/microsky/blob/master/microsky.py")

Example
-----------------

Here is an example of doing the following

- Retrieving a list of your posts
- Post
- Delete a post

::

   import microsky

   with microsky.createSession("xxx.bsky.social", "password") as session:
       print(session.listPosts(did=session.did))
       post = session.sendPost("Hello Bluesky!")
       print(post)
       print(session.listPosts(did=session.did))
       print("delete")
       print(session.deletePost(post["uri"]))
       print(session.listPosts(did=session.did))

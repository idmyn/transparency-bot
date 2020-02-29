transparency_bot
================

This is a Telegram bot that listens for messages containing images, resizes them
if necessary (to fit the Telegram sticker restriction of 512 pixels), replaces
white pixels with transparency, and returns the modified image to the sender.

commands
--------

::

  poetry run bot
  poetry run pytest

# srt-to-html

A simple Python script that converts a subtitle file (SRT) into HTML, creating a readable web page transcript.

## Usage

This script was written for Japanese language learning. It takes an SRT file extracted from a YouTube video **insert suggested tool here** and converts it into a transcript that can be read along with video playback. Conversion to an HTML page allows automatic insertion of furigana in the transcript with a browser add-on such as [Furiganator](https://chromewebstore.google.com/detail/furiganator/ijfcmmkkmogaclaafpgcjdfcfibmhcfa?pli=1) (Chrome) or [Furiganaize](https://addons.mozilla.org/en-US/firefox/addon/furiganaize/) (Firefox).

**srt-to-html** can be used for any language, not just Japanese. Note that the HTML page language attribute in this script is for Japanese. Depending on your use case (e.g., screen readers, spell checking), this attribute may need to be changed in the script when working with a different language. To do so, look for the following line:

`<html lang="ja" dir="auto">`

Change the `ja` attribute to the tag for your target language. [A list of common tags](https://en.wikipedia.org/wiki/IETF_language_tag#List_of_common_primary_language_subtags) is available on Wikipedia.

## Example Workflow

[expand and write this out]

Download YouTube Transcript https://chromewebstore.google.com/detail/download-youtube-transcri/popcechepbjbgkpobdjhggdecojbgpco
Youtube Subtitle Downloader https://addons.mozilla.org/en-US/firefox/addon/youtube-subtitle-downloader/

## Compatibility

[to be completed]
# srt-to-html

A simple Python script that converts a subtitle file (SRT) into HTML, creating a readable web page transcript.

## Usage

This script was written for Japanese language listening practice using videos. It takes a subtitle (SRT) file extracted from a YouTube video and converts it into a transcript that can be read along with video playback. Conversion to an HTML page allows automatic insertion of furigana in the transcript with a browser add-on such as [Furiganator](https://chromewebstore.google.com/detail/furiganator/ijfcmmkkmogaclaafpgcjdfcfibmhcfa?pli=1) (Chrome) or [Furiganaize](https://addons.mozilla.org/en-US/firefox/addon/furiganaize/) (Firefox).

### Requirement

Requires a [Python installation](https://www.python.org/downloads/).

### Usable with Most Languages

**srt-to-html** can be used for most any language, not just Japanese. Note that the HTML page language attribute in this script is for Japanese. Depending on your use case (e.g., screen readers, spell checking), this attribute may need to be changed in the script when working with a different language. To do so, look for the following line:

`<html lang="ja" dir="auto">`

Change the `ja` attribute to the tag for your target language. [A list of common tags](https://en.wikipedia.org/wiki/IETF_language_tag#List_of_common_primary_language_subtags) is available on Wikipedia.

## Workflow Example

Here is an example of a typical workflow using this script:

1. Create an SRT file from a YouTube video with the method of your choice (some options are [Download YouTube Transcript](https://chromewebstore.google.com/detail/download-youtube-transcri/popcechepbjbgkpobdjhggdecojbgpco) for Chrome or [Youtube Subtitle Downloader](https://addons.mozilla.org/en-US/firefox/addon/youtube-subtitle-downloader/) for Firefox).
2. Drag-and-drop the SRT file onto **srt-to-html.py**. The HTML file will be output in the same folder.
3. Open the HTML file in Firefox and activate Furiganaize.

## Compatibility

There are some potential unexpected outputs or errors that may arise when running this script.

* **Nonstandard SRT variants**: some SRT files use dot separators for milliseconds (00:00:00.000), extra spaces, markers, or unusual timecode spacing. Try using a different generator for your SRT file if the transcript is malformed.

* **Additional metadata lines**: SRTs can include notes like `<i>text</i>` HTML tags, speaker labels, or hearing-impaired cues. This script will still preserve this metadata.

* **Encoding**: older SRTs may be in Windows-1252, Shift_JIS, or other encodings. Files must be converted to UTF‑8 first.

## Sample Output

Before:

```srt
1
00:00:00,000 --> 00:00:03,000
皆さん、こんにちは。

2
00:00:03,000 --> 00:00:09,000
私の夫の家族はアメリカに住んでいます。

3
00:00:09,000 --> 00:00:13,000
家族はアメリカにいます。

...
```

After:

```html
<html lang="ja" dir="auto">
<head>
    ...
</head>
<p>皆さん、こんにちは。</p>
<p>私の夫の家族はアメリカに住んでいます。</p>
<p>家族はアメリカにいます。</p>

...
```

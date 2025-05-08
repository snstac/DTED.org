# Usage

## Android Team Awareness Kit (ATAK)

DTED.org offers two integration methods with ATAK:

1. **DTED Stream Server**

   ATAK with no plugin required. Operates as a drop-in replacement for ATAK's default DTED Stream Server (TPC).

2. **Simple DTED Streamer**

   ATAK with [Simple DTED Streamer](https://tak.gov/plugins/simple-dted-streamer) plugin. Operates as a Simple DTED Server.


### 1. Automatically with a QR Code

Scan the following QR code using the camera on your ATAK device (use the Android camera app, not ATAK QuickCam):

![ATAK DTED QR code for California](https://CA.DTED.org/CA-QR.png)

### 2. Manually via ATAK

[TK]

### 3. Using an ATAK Preferences File

Add the following entries to your ATAK preferences file:

```xml
<entry key="prefs_dted_stream_server" class="class java.lang.String">CA.DTED.org</entry>
<entry key="simpleDtedStreamer.streaming_dted_uri_key" class="class java.lang.String">https://CA.DTED.org</entry>
<entry key="prefs_dted_stream" class="class java.lang.Boolean">true</entry>
```

[Sample ATAK preferences file](https://ca.dted.org/CA.DTED.org.pref).

## WinTAK

TK

## TAKX

TK

## iTAK

TK

## Other Tools

For California **(explicit values for ATAK)**:

* DTED Stream Server: `CA.DTED.org`

* Simple DTED Server: `https://CA.DTED.org`

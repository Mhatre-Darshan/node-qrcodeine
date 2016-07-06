{
  "targets": [
    {
      "target_name": "qrcodeine",
      "sources": [ "src/qrcodeine.cc" ],
      "libraries": ["-lqrencode", "-lpng"],
      "include_dirs" : [
        "<!(node -e \"require('nan')\")"
      ]
    }
  ],
}

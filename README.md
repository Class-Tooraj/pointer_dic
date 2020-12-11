# PointerDic
* example to encrypting & decrypting data
Build a specific point dictionary to translate from the previous point to the new one. [ This is an example ]
# CFI DOC -> main.py

 * ALL INPUT CMD SUPPORT:
        /I: change intro [list]
        /F: update focus [int]
        /R: reversed map [int]
        >>: focus up [int] , default= 1
        <<: focus down [int] , default= 1
        +: add items to map [list]
        -: sub items from map [list]
        /reset: reset to default
        ----
        en: encrypt data
        de: decrypt data

  *  pattern:/support command/
        /All command support/-> [cmd][value]
        /Only 'en' & 'de'/-> [cmd]

  *  example:/use command/
       All available -> '/F 3' |mean update focus to 3
       en & de -> 'en' |mean set to encrypt mode for one[1] period encrypt
# POINTERDIC DOC -> pointerdic.py
  * PointerDic -- init:
         Create Dic use PointerDic Protocol
        * param intro: if dict must be start from '0' example: {0: 'A', 1: 'B', ...} or ['A', 'B']
          default intro: ASCII -> idx 0, idx 127
          type intro: -list-, -dict-
        * param focus: choice index for focusing value
          default focus: 0
          type focus: -int-

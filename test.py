from tesserocr import PyTessBaseAPI, RIL, iterate_level

def get_font(image_path):
    with PyTessBaseAPI() as api:
        api.SetImageFile(image_path)
        api.Recognize()
        ri = api.GetIterator()
        level = RIL.SYMBOL

        for r in iterate_level(ri, level):
            symbol = r.GetUTF8Text(level)
            word_attributes = r.WordFontAttributes()

            if symbol:
                 print (u'symbol {}, font: {}'.format(symbol, word_attributes['font_name']))

get_font('logo.jpg')

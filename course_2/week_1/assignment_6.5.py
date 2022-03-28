text = "X-DSPAM-Confidence: 0.8475"
position = text.find("0")
number = text[position:]
number = float(number)
print(number)

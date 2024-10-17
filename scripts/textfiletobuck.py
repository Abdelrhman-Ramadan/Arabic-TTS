import json
import argparse

# Buckwalter mapping
buckwalter = {
    u'\u0628': u'b', u'\u0632': u'z', u'\u0630': u'*', u'\u0637': u'T', u'\u0645': u'm',
    u'\u062a': u't', u'\u0631': u'r', u'\u0638': u'Z', u'\u0646': u'n',
    u'\u062b': u'^', u'\u0639': u'E', u'\u0647': u'h', u'\u062c': u'j',
    u'\u0633': u's', u'\u063a': u'g', u'\u062d': u'H', u'\u0642': u'q',
    u'\u0641': u'f', u'\u062e': u'x', u'\u0635': u'S', u'\u0634': u'$',
    u'\u062f': u'd', u'\u0636': u'D', u'\u0643': u'k', u'\u0623': u'>',
    u'\u0621': u'\'', u'\u0626': u'}', u'\u0624': u'&', u'\u0625': u'<',
    u'\u0622': u'|', u'\u0627': u'A', u'\u0649': u'Y', u'\u0629': u'p',
    u'\u064a': u'y', u'\u0644': u'l', u'\u0648': u'w', u'\u064b': u'F',
    u'\u064c': u'N', u'\u064d': u'K', u'\u064e': u'a', u'\u064f': u'u',
    u'\u0650': u'i', u'\u0651': u'~', u'\u0652': u'o'
}

def arabicToBuckwalter(word):
    res = u''
    for letter in word:
        if letter in buckwalter:
            res += buckwalter[letter]
        else:
            res += letter
    return res

def main(json_file_path, output_file_path):
    # Read from JSON and write to output file
    with open(json_file_path, mode='r', encoding='utf-8') as json_file, open(output_file_path, mode='w', encoding='utf-8') as output_file:
        data = json.load(json_file)

        for item in data:
            audio_file = item['audio_file']   # Get the audio file name
            arabic_text = item['text']        # Get the Arabic text
            buckwalter_text = arabicToBuckwalter(arabic_text)

            # Write to output file
            output_file.write(f'[{audio_file}] "[{buckwalter_text}]"' + '\n')

    print("Output file created successfully!")

if __name__ == "__main__":
    # Argument parsing
    parser = argparse.ArgumentParser(description="Convert Arabic text in a JSON file to Buckwalter and save output to a file.")
    parser.add_argument('json_file_path', type=str, help="Path to the input JSON file")
    parser.add_argument('output_file_path', type=str, help="Path to the output file")

    args = parser.parse_args()

    # Call the main function with the parsed arguments
    main(args.json_file_path, args.output_file_path)

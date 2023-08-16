import csv


def converter(arquivo_csv, arquivo_vcard):
    with open(arquivo_csv, 'r', encoding="UTF-8") as csvfile, open(arquivo_vcard, 'w', encoding="UTF-8") as vcardfile:
        csvreader = csv.reader(csvfile)
        next(csvreader)  # Pula cabecalho

        for row in csvreader:
            Name,GivenName, Number = row
            vcard = f"BEGIN:VCARD\nVERSION:3.0\nN:;{Name};;;\nFN:{GivenName}\nTEL;type=CELL;type=VOICE;type=PREF:{Number}\nEND:VCARD\n"
            vcardfile.write(vcard)

    print("Conversion complete.")


if __name__ == "__main__":
    arquivo_csv = "C:\\Suporte\\Telefonia\\contactsgoogle.csv"  #
    arquivo_vcard = "C:\\Suporte\\Telefonia\\ContactsGoogleConvertidoAgoraVai.vcf"
    converter(arquivo_csv, arquivo_vcard)

# Dies ist ein harmloses Testskript, das den Eikei Testvirus String ausgibt
# Es sollte von Antivirenprogrammen als Virus erkannt werden
# Es richtet keinen Schaden an und zeigt nur eine Meldung auf dem Bildschirm an
# Es erstellt auch eine ausführbare Datei, die sich 100 mal selbst kopiert mit verschiedenen Erweiterungen
# https://heimdall-security.net/
# https://github.com/Brainhub24/Testvirus


# Der Eikei Testvirus String
test_virus = b"X5O!P%@AP[4\\PZX54(P^)7CC)7}$EICAR-STANDARD-ANTIVIRUS-TEST-FILE!$H+H*"

# Die Meldung, die angezeigt wird
message = "Test Virus erfolgreich ausgeführt!"

# Die Datei, in die der String geschrieben wird
file_name = "test_virus.com"

# Die Datei öffnen und den String schreiben
with open(file_name, "wb") as f:
    f.write(test_virus)

# Die Meldung ausgeben
print(message)

# Die Anzahl der Kopien
copies = 100

# Eine Liste von möglichen Erweiterungen
extensions = [".exe", ".bat", ".txt", ".png", ".jpg", ".jpeg"]

# Eine Schleife, um die Datei zu kopieren
for i in range(copies):
    # Eine zufällige Erweiterung auswählen
    import random
    extension = random.choice(extensions)
    # Der Name der Kopie
    copy_name = f"test_virus_{i+1}{extension}"
    # Die Kopie erstellen
    with open(copy_name, "wb") as f:
        f.write(test_virus)

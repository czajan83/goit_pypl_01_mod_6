# goit_pypl_01_mod_6

Skrypt atomatyzuje sortowanie plików z wybranowego folderu
Posortowane pliki umieszcza na pulpicie Twojego systemu w folderze sorted
Zamienia wszelkie znaki diakrytyczne i inne niestandardowe znaki w nazawach plików na znak podkreślenia "_"
Nie zmienia znaków w rozszerzeniach plików
Rozpakowuje archiwa zip, tar oraz gz

Zawartość:
start_conditions_tests - testy jednostkowe sprawdzające kompletność wzorcowego zestawu plików - tylko do developmentu
working_script_tests - testy jednostkowe dla funkcji znajdujących się w skrypcie sort.py
sort.py - skrypt wykonujący sortowanie plików 

Wymagania:
System operacyjny Windows 10 (nie sprawdzano w innych wersjach systemu windows)
Interpreter Python w wersji 3.11 (nie sprawdzano w innych wersjach interpretera)

Uruchomienie:
Sklonuj zawartość repozytorium do wybranego folderu na Twoim dysku
Uruchom wiersz linii poleceń (cmd)
Przejdź do folderu do którego sklonowano zawartość repozytorium
Wprowadź z klawiatury polecenie "python sort.py <path>" gdzie <path> - ścieżka do folderu, który chcesz uporządkować
<path> jest składnikiem opcjonalnym, w przypadku wydania polecenia "python sort.py" skrypt posortuje pliki znajdujące się w folderze "to_review" na Twoim pulpicie


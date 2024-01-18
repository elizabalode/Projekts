Automatizācijas Projekts
Projekta Uzdevums:
    Šis projekts izmanto Selenium bibliotēku Python valodā, lai automatizētu nekustamā īpašuma meklēšanas procesu. Projekta mērķis ir veikt automātisku meklēšanu, kā arī iegūt un saglabāt attēlu URL no izvēlētā paziņojuma.
Izmantotās bibliotēkas
    Selenium: Automatizācijas rīks, kas tiek izmantots, lai pārlūkotu un veiktu darbības tīmekļa vietnē.
    WebDriver: Bibliotēka, kas nodrošina iespēju kontrolēt pārlūku programmātiski.
    WebDriverWait: Palīgrīks, kas ļauj gaidīt līdz noteiktam nosacījumam tiek izpildīts pirms turpināt darbību.
Programmatūras Izmantošanas Metodes
1.Pirmkārt, tiek atvērta City24.lv vietne un tiek noraidīti sīkdatņu piekrītumi.
2.Meklēšanas laukumā tiek ievadīta atrašanās vieta, un tiek atlasīts pirmais atbilstošais rezultāts.
3.Rezultāti tiek sakārtoti pēc cenas augošā secībā, un tiek uzspiests kārtošanas poga.
4.Atverot pirmo rezultātu, tiek iegūts attēla URL un saglabāts failā "url_list.txt".

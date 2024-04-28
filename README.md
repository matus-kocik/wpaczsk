# wpaczsk
World Pheasant Association Czech Republic and Slovakia

# Database Model

## 1. Role
- `id` (IntegerField): Primary key. // Primárny kľúč.
- `name` (CharField): Name of the role, e.g., "admin" or "user". // Názov role, napríklad "admin" alebo "užívateľ".

## 2. User
- `id` (IntegerField): Primary key. // Primárny kľúč.
- `role_id` (ForeignKey): Connection to the Role table. // Kľúč pre spojenie s tabuľkou Role.
- `first_name` (CharField): User's first name. // Krstné meno užívateľa.
- `last_name` (CharField): User's last name. // Priezvisko užívateľa.
- `username` (CharField): User's chosen name for login. // Používateľské meno.
- `email` (EmailField): User's email address. // Emailová adresa.
- `password` (CharField): Password (stored as a hash). // Heslo užívateľa (uložené ako hash).
- `profile_picture` (ImageField): Link to the user's profile image. // Profilová fotografia.
- `mobile_phone` (CharField): User's mobile phone number. // Mobilné telefónne číslo.
- `address` (CharField): User's residence address. // Adresa bydliska.
- `city` (CharField): City of residence. // Mesto bydliska.
- `country` (CharField): Country of residence. // Krajina bydliska.

## 3. Species
- `id` (IntegerField): Primary key. // Primárny kľúč.
- `latin_name` (CharField): Latin name of the species. // Latinský názov druhu.
- `czech_name` (CharField): Czech name of the species. // Český názov druhu.
- `slovak_name` (CharField): Slovak name of the species. // Slovenský názov druhu.
- `conservation_status` (CharField): Conservation status of the species. // Stav ochrany druhu.
- `habitat` (TextField): The natural habitat of the species. // Biotop, kde druh žije.
- `average_lifespan` (IntegerField): The average lifespan of the species. // Priemerná dĺžka života druhu.
- `description` (TextField): Description of the species. // Popis druhu.
- `images` (CharField): Links to images associated with the species. // Obrázky súvisiace s druhom.
- `url_video` (URLField): Link to a video associated with the species. // Odkaz na video súvisiace s druhom.

## 4. Subspecies
- `id` (IntegerField): Primary key. // Primárny kľúč.
- `species_id` (ForeignKey): Connection to the Species table. // Kľúč pre spojenie s tabuľkou Species.
- `latin_name` (CharField): Latin name of the subspecies. // Latinský názov poddruhu.
- `czech_name` (CharField): Czech name of the subspecies. // Český názov poddruhu.
- `slovak_name` (CharField): Slovak name of the subspecies. // Slovenský názov poddruhu.
- `conservation_status` (CharField): Conservation status of the subspecies. // Stav ochrany poddruhu.
- `habitat` (TextField): The natural habitat of the subspecies. // Biotop poddruhu.
- `average_lifespan` (IntegerField): The average lifespan of the subspecies. // Priemerná dĺžka života poddruhu.
- `description` (TextField): Description of the subspecies. // Popis poddruhu.
- `images` (CharField): Links to images associated with the subspecies. // Obrázky súvisiace s poddruhom.
- `url_video` (URLField): Link to a video associated with the subspecies. // Odkaz na video súvisiace s poddruhom.

## 5. Breeding Record
-- `id` (IntegerField): Primary key. // Primárny kľúč.
- `breeder_id` (ForeignKey to User): The user responsible for the breeding. // Užívateľ zodpovedný za chov.
- `subspecies_id` (ForeignKey to Subspecies): The subspecies being bred. // Poddruh, ktorý sa chová.
- `year` (IntegerField): The year of the breeding record. // Rok, pre ktorý je záznam o chove.
- `number_of_males` (IntegerField): Number of male animals. // Počet samcov.
- `number_of_females` (IntegerField): Number of female animals. // Počet samíc.
- `number_of_species` (IntegerField): Total number of species bred. // Celkový počet chovaných druhov.
- `total_offsprings` (IntegerField): Total number of offsprings produced. // Celkový počet produkovaných potomkov.
- `notes` (TextField): Additional notes about the breeding. // Dodatočné poznámky o chove.

## 6. Event
- `id` (IntegerField): Primary key. // Primárny kľúč.
- `name` (CharField): Name of the event. // Názov udalosti.
- `date_from` (DateField): Start date and time of the event. // Dátum a čas začiatku udalosti.
- `date_to` (DateField): End date and time of the event. // Dátum a čas konca udalosti.
- `url` (URLField): Web link with information about the event. // Webový odkaz s informáciami o udalosti.
- `location` (CharField): Venue of the event. // Miesto konania udalosti.
- `description` (TextField): Detailed description of the event. // Podrobný popis udalosti.

## 7. Article
- `id` (IntegerField): Primary key. // Primárny kľúč.
- `title` (CharField): Title of the article. // Titulok článku.
- `pdf_file` (FileField): Link to the article's PDF file. // Odkaz na PDF súbor článku.
- `publication_date` (DateField): Date of article publication. // Dátum publikácie článku.
- `author_id` (ForeignKey to User): Reference to the author of the article in the User table. // Referencia na autora článku v tabuľke užívateľov.

## 8. Breeding Record
- `id` (IntegerField): Primary key. // Primárny kľúč.
- `breeder_id` (ForeignKey to User): The user responsible for the breeding. // Užívateľ zodpovedný za chov.
- `subspecies_id` (ForeignKey to Subspecies): The subspecies being bred. // Poddruh, ktorý sa chová.
- `year` (IntegerField): The year the record was made. // Rok, kedy bol záznam vytvorený.
- `number_of_males` (IntegerField): Number of male animals. // Počet samcov.
- `number_of_females` (IntegerField): Number of female animals. // Počet samíc.
- `number_of_species` (IntegerField): Total number of species bred. // Celkový počet chovaných druhov.
- `total_offsprings` (IntegerField): Total number of offsprings produced. // Celkový počet produkovaných potomkov.
- `notes` (TextField): Additional notes about the breeding. // Dodatočné poznámky k chovu.

## 9. Event
- `id` (IntegerField): Primary key. // Primárny kľúč.
- `name` (CharField): Name of the event. // Názov udalosti.
- `date_from` (DateField): Start date and time of the event. // Dátum a čas začiatku udalosti.
- `date_to` (DateField): End date and time of the event. // Dátum a čas konca udalosti.
- `url` (URLField): Web link with information about the event. // Webový odkaz s informáciami o udalosti.
- `location` (CharField): Venue of the event. // Miesto konania udalosti.
- `description` (TextField): Detailed description of the event. // Podrobný popis udalosti.

## 10. Article
- `id` (IntegerField): Primary key. // Primárny kľúč.
- `title` (CharField): Title of the article. // Titulok článku.
- `pdf_file` (FileField): Link to the article's PDF file. // Odkaz na PDF súbor článku.
- `publication_date` (DateField): Date of article publication. // Dátum publikácie článku.
- `author_id` (ForeignKey to User): Reference to the article's author. // Odkaz na autora článku.



# wpaczsk
World Pheasant Association Czech Republic and Slovakia

# Database Model

## Accounts:
### 1. Role
- `id` (IntegerField): Primary key. // Primárny kľúč.
- `name` (CharField): Name of the role, e.g., "admin" or "user". // Názov role, napríklad "admin" alebo "užívateľ".
- `created_at` (DateTimeField): Record creation time. // Čas vytvorenia záznamu.
- `updated_at` (DateTimeField): Record last update time. // Čas poslednej aktualizácie záznamu.
- `deleted_at` (DateTimeField): Record deletion time, if soft deleted. // Čas zmazania záznamu, ak ide o mäkké zmazanie.

### 2. User
- `id` (IntegerField): Primary key. // Primárny kľúč.
- `role_id` (ForeignKey to Role): Connection to the Role table. // Kľúč pre spojenie s tabuľkou Role.
- `registration_number` (IntegerField): Unique registration number for breeders. // Jedinečné registrační číslo pro chovatele.
- `first_name` (CharField): User's first name. // Krstné meno užívateľa.
- `last_name` (CharField): User's last name. // Priezvisko užívateľa.
- `username` (CharField): User's chosen name for login. // Používateľské meno.
- `email` (EmailField): User's email address. // Emailová adresa.
- `password` (CharField): Password (stored as a hash). // Heslo užívateľa (uložené ako hash).
- `profile_picture` (ImageField): Link to the user's profile image. // Profilová fotografia.
- `mobile_phone` (CharField): User's mobile phone number. // Mobilné telefónne číslo.
- `address` (CharField): User's residence address. // Adresa bydliska.
- `city` (CharField): City of residence. // Mesto bydliska.
- `country` (ForeignKey to Country): Reference to the country table. // Odkaz na tabuľku krajiny.
- `created_at` (DateTimeField): Record creation time. // Čas vytvorenia záznamu.
- `updated_at` (DateTimeField): Record last update time. // Čas poslednej aktualizácie záznamu.
- `deleted_at` (DateTimeField): Record deletion time, if soft deleted. // Čas zmazania záznamu, ak ide o mäkké zmazanie.

## SpeciesHub:
### 3. Species
- `id` (IntegerField): Primary key. // Primárny kľúč.
- `latin_name` (CharField): Latin name of the species. // Latinský názov druhu.
- `czech_name` (CharField): Czech name of the species. // Český názov druhu.
- `slovak_name` (CharField): Slovak name of the species. // Slovenský názov druhu.
- `conservation_status` (CharField): Conservation status of the species. // Stav ochrany druhu.
- `habitat` (TextField): The natural habitat of the species. // Biotop, kde druh žije.
- `average_lifespan` (IntegerField): The average lifespan of the species. // Priemerná dĺžka života druhu.
- `description` (TextField): Description of the species. // Popis druhu.
- `ring_size_id` (ForeignKey to Ring Size): Reference to a ring size. // Referencia na veľkosť kružku.
- `videos` (ManyToManyField to Video): Multiple videos can be linked. // Video súvisiace s druhom.
- `url_video` (URLField): Link to a video associated with the species. // Odkaz na video súvisiace s druhom.
- `tags` (ManyToManyField to Tag): Tags associated with the species. // Značky priradené k druhu.
- `categories` (ManyToManyField to Category): Categories associated with the species. // Kategórie priradené k druhu.
- `created_at` (DateTimeField): Record creation time. // Čas vytvorenia záznamu.
- `updated_at` (DateTimeField): Record last update time. // Čas poslednej aktualizácie záznamu.
- `deleted_at` (DateTimeField): Record deletion time, if soft deleted. // Čas zmazania záznamu, ak ide o mäkké zmazanie.

### 4. Subspecies
- `id` (IntegerField): Primary key. // Primárny kľúč.
- `species_id` (ForeignKey to Species): Connection to the Species table. // Kľúč pre spojenie s tabuľkou Species.
- `latin_name` (CharField): Latin name of the subspecies. // Latinský názov poddruhu.
- `czech_name` (CharField): Czech name of the subspecies. // Český názov poddruhu.
- `slovak_name` (CharField): Slovak name of the subspecies. // Slovenský názov poddruhu.
- `conservation_status` (CharField): Conservation status of the subspecies. // Stav ochrany poddruhu.
- `habitat` (TextField): The natural habitat of the subspecies. // Biotop poddruhu.
- `average_lifespan` (IntegerField): The average lifespan of the subspecies. // Priemerná dĺžka života poddruhu.
- `description` (TextField): Description of the subspecies. // Popis poddruhu.
- `ring_size_id` (ForeignKey to Ring Size): Reference to a ring size. // Referencia na veľkosť kružku.
- `images` (ManyToManyField to Image): Multiple images can be linked. // Obrázky súvisiace s poddruhom.
- `videos` (ManyToManyField to Video): Multiple videos can be linked. // Video súvisiace s poddruhom.
- `url_video` (URLField): Link to a video associated with the subspecies. // Odkaz na video súvisiace s podruhom.
- `tags` (ManyToManyField to Tag): Tags associated with the subspecies. // Značky priradené k poddruhu.
- `categories` (ManyToManyField to Category): Categories associated with the subspecies. // Kategórie priradené k poddruhu.
- `created_at` (DateTimeField): Record creation time. // Čas vytvorenia záznamu.
- `updated_at` (DateTimeField): Record last update time. // Čas poslednej aktualizácie záznamu.
- `deleted_at` (DateTimeField): Record deletion time, if soft deleted. // Čas zmazania záznamu, ak ide o mäkké zmazanie.

## Breeding:
### 5. Breeding Record
-- `id` (IntegerField): Primary key. // Primárny kľúč.
- `breeder_id` (ForeignKey to User): The user responsible for the breeding. // Užívateľ zodpovedný za chov.
- `species_id` (ForeignKey to Species): Connection to the Species table. // Kľúč pre spojenie s tabuľkou Species.
- `subspecies_id` (ForeignKey to Subspecies): The subspecies being bred. // Poddruh, ktorý sa chová.
- `year` (IntegerField): The year of the breeding record. // Rok, pre ktorý je záznam o chove.
- `number_of_males` (IntegerField): Number of male animals. // Počet samcov.
- `number_of_females` (IntegerField): Number of female animals. // Počet samíc.
- `number_of_species` (IntegerField): Total number of species bred. // Celkový počet chovaných druhov.
- `total_offsprings` (IntegerField): Total number of offsprings produced. // Celkový počet produkovaných potomkov.
- `notes` (TextField): Additional notes about the breeding. // Dodatočné poznámky o chove.
- `created_at` (DateTimeField): Record creation time. // Čas vytvorenia záznamu.
- `updated_at` (DateTimeField): Record last update time. // Čas poslednej aktualizácie záznamu.
- `deleted_at` (DateTimeField): Record deletion time, if soft deleted. // Čas zmazania záznamu, ak ide o mäkké zmazanie.

### 6. Ring
- `id` (IntegerField): Primary key. // Primárny kľúč.
- `size` (FloatField): Size of the ring. // Veľkosť kružku.

## Events:
### 7. Event
- `id` (IntegerField): Primary key. // Primárny kľúč.
- `name` (CharField): Name of the event. // Názov udalosti.
- `date_from` (DateField): Start date and time of the event. // Dátum a čas začiatku udalosti.
- `date_to` (DateField): End date and time of the event. // Dátum a čas konca udalosti.
- `url` (URLField): Web link with information about the event. // Webový odkaz s informáciami o udalosti.
- `location` (ForeignKey to Location): Reference to the Location model. // Odkaz na model.
- `description` (TextField): Detailed description of the event. // Podrobný popis udalosti.
- `created_at` (DateTimeField): Record creation time. // Čas vytvorenia záznamu.
- `updated_at` (DateTimeField): Record last update time. // Čas poslednej aktualizácie záznamu.
- `deleted_at` (DateTimeField): Record deletion time, if soft deleted. // Čas zmazania záznamu, ak ide o mäkké zmazanie.

## Content:
### 8. Article
- `id` (IntegerField): Primary key. // Primárny kľúč.
- `title` (CharField): Title of the article. // Titulok článku.
- `pdf_file` (FileField): Link to the article's PDF file. // Odkaz na PDF súbor článku.
- `image_files` (ImageField): Links to images associated with the article. // Odkazy na obrázky spojené s článkom.
- `publication_date` (DateField): Date of article publication. // Dátum publikácie článku.
- `author` (ForeignKey to User): Reference to the article's author. // Odkaz na autora článku.
- `created_at` (DateTimeField): Record creation time. // Čas vytvorenia záznamu.
- `updated_at` (DateTimeField): Record last update time. // Čas poslednej aktualizácie záznamu.
- `deleted_at` (DateTimeField): Record deletion time, if soft deleted. // Čas zmazania záznamu, ak ide o mäkké zmazanie.

### 9. Comment
- `id` (IntegerField): Primary key. // Primárny kľúč.
- `content_type` (ForeignKey): Reference to the type of content (article, species record, etc.). // Odkaz na typ obsahu (článok, záznam o druhu, atď.).
- `object_id` (IntegerField): ID of the content to which the comment is attached. // ID obsahu, ku ktorému je komentár priradený.
- `content` (TextField): The text of the comment. // Text komentára.
- `user` (ForeignKey to User): The user who posted the comment. // Užívateľ, ktorý komentár pridal.
- `created_at` (DateTimeField): The date and time the comment was created. // Dátum a čas vytvorenia komentára.
- `updated_at` (DateTimeField): The date and time the comment was last updated. // Dátum a čas poslednej aktualizácie komentára.

### 10. Rating
- `id` (IntegerField): Primary key. // Primárny kľúč.
- `content_type` (ForeignKey): Reference to the type of content (article, species record, etc.). // Odkaz na typ obsahu (článok, záznam o druhu, atď.).
- `object_id` (IntegerField): ID of the content being rated. // ID obsahu, ktorý sa hodnotí.
- `rating` (IntegerField): The score given, typically on a scale from 1 to 5. // Hodnotenie udelené, typicky na škále od 1 do 5.
- `user` (ForeignKey to User): The user who posted the rating. // Užívateľ, ktorý hodnotenie pridal.
- `created_at` (DateTimeField): The date and time the rating was created. // Dátum a čas vytvorenia hodnotenia.

## Classification:
### 11. Tag
- `id` (IntegerField): Primary key. // Primárny kľúč.
- `name` (CharField): Name of the tag. // Názov značky.
- `description` (TextField): Description of the tag. // Popis značky.

### 12. Category
- `id` (IntegerField): Primary key. // Primárny kľúč.
- `name` (CharField): Name of the category. // Názov kategórie.
- `description` (TextField): Description of the category. // Popis kategórie.

## Geography:
### 13. Country
- `id` (IntegerField): Primary key. // Primárny kľúč.
- `name` (CharField): Name of the country. // Názov krajiny.
- `code` (CharField): ISO code of the country, e.g., 'SK' for Slovakia. // ISO kód krajiny, napr. 'SK' pre Slovensko.
- `created_at` (DateTimeField): Record creation time. // Čas vytvorenia záznamu.
- `updated_at` (DateTimeField): Record last update time. // Čas poslednej aktualizácie záznamu.
- `deleted_at` (DateTimeField): Record deletion time, if soft deleted. // Čas zmazania záznamu, ak ide o mäkké zmazanie.

### 14. Location
- `id` (IntegerField): Primary key. // Primárny kľúč.
- `name` (CharField): Name of the location. // Názov lokácie.
- `country`  (ForeignKey to Country): Reference to the Country model. // Odkaz na model Country.
- `latitude` (FloatField): Latitude for the event location. // Zemepisná šírka miesta konania.
- `longitude` (FloatField): Longitude for the event location. // Zemepisná dĺžka miesta konania.
- `created_at` (DateTimeField): Record creation time. // Čas vytvorenia záznamu.
- `updated_at` (DateTimeField): Record last update time. // Čas poslednej aktualizácie záznamu.
- `deleted_at` (DateTimeField): Record deletion time, if soft deleted. // Čas zmazania záznamu, ak ide o mäkké zmazanie.

## Media:
### 15. Image
- `id` (IntegerField): Primary key. // Primárny kľúč.
- `image` (ImageField): The image file. // Súbor obrázka.
- `description` (TextField, optional): Description of the image. // Popis obrazka, nepovinné.
- `content_type` (ForeignKey to ContentType): Generic relationship to any model. // Generický vzťah k ľubovoľnému modelu.
- `object_id` (PositiveIntegerField): ID of the related object. // ID príslušného objektu.
- `content_object` (GenericForeignKey): Generic foreign key pointing to the related object. // Generický cudzí kľúč ukazujúci na príslušný objekt.
- `created_at` (DateTimeField): Record creation time. // Čas vytvorenia záznamu.
- `updated_at` (DateTimeField): Record last update time. // Čas poslednej aktualizácie záznamu.
- `deleted_at` (DateTimeField, optional): Record deletion time, if soft deleted. // Čas zmazania záznamu, ak ide o mäkké zmazanie.

### Video
- `id` (IntegerField): Primary key. // Primárny kľúč.
- `video` (FileField): The video file. // Súbor videa.
- `title` (CharField, optional): Title of the video. // Názov videa, nepovinné.
- `description` (TextField, optional): Description of the video. // Popis videa, nepovinné.
- `content_type` (ForeignKey to ContentType): Generic relationship to any model. // Generický vzťah k ľubovoľnému modelu.
- `object_id` (PositiveIntegerField): ID of the related object. // ID príslušného objektu.
- `content_object` (GenericForeignKey): Generic foreign key pointing to the related object. // Generický cudzí kľúč ukazujúci na príslušný objekt.
- `created_at` (DateTimeField): Record creation time. // Čas vytvorenia záznamu.
- `updated_at` (DateTimeField): Record last update time. // Čas poslednej aktualizácie záznamu.
- `deleted_at` (DateTimeField, optional): Record deletion time, if soft deleted. // Čas zmazania záznamu, ak ide o mäkké zmazanie.

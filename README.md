# WPAczsk
World Pheasant Association Czech Republic and Slovakia

## Content:
### Article
- `id` (IntegerField): Primary key. // Primárny kľúč.
- `title` (CharField): Title of the article. // Titulok článku.
- `pdf_file` (FileField): Link to the article's PDF file. // Odkaz na PDF súbor článku.
- `image_files` (ImageField): Links to images associated with the article. // Odkazy na obrázky spojené s článkom.
- `publication_date` (DateField): Date of article publication. // Dátum publikácie článku.
- `author` (ForeignKey to User): Reference to the article's author. // Odkaz na autora článku.
- `created_at` (DateTimeField): Record creation time. // Čas vytvorenia záznamu.
- `updated_at` (DateTimeField): Record last update time. // Čas poslednej aktualizácie záznamu.
- `deleted_at` (DateTimeField): Record deletion time, if soft deleted. // Čas zmazania záznamu, ak ide o mäkké zmazanie.

### Event
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

### Comment
- `id` (IntegerField): Primary key. // Primárny kľúč.
- `content_type` (ForeignKey): Reference to the type of content (article, species record, etc.). // Odkaz na typ obsahu (článok, záznam o druhu, atď.).
- `object_id` (IntegerField): ID of the content to which the comment is attached. // ID obsahu, ku ktorému je komentár priradený.
- `content` (TextField): The text of the comment. // Text komentára.
- `user` (ForeignKey to User): The user who posted the comment. // Užívateľ, ktorý komentár pridal.
- `created_at` (DateTimeField): The date and time the comment was created. // Dátum a čas vytvorenia komentára.
- `updated_at` (DateTimeField): The date and time the comment was last updated. // Dátum a čas poslednej aktualizácie komentára.

### Rating
- `id` (IntegerField): Primary key. // Primárny kľúč.
- `content_type` (ForeignKey): Reference to the type of content (article, species record, etc.). // Odkaz na typ obsahu (článok, záznam o druhu, atď.).
- `object_id` (IntegerField): ID of the content being rated. // ID obsahu, ktorý sa hodnotí.
- `rating` (IntegerField): The score given, typically on a scale from 1 to 5. // Hodnotenie udelené, typicky na škále od 1 do 5.
- `user` (ForeignKey to User): The user who posted the rating. // Užívateľ, ktorý hodnotenie pridal.
- `created_at` (DateTimeField): The date and time the rating was created. // Dátum a čas vytvorenia hodnotenia.

## Classification:
### Tag
- `id` (IntegerField): Primary key. // Primárny kľúč.
- `name` (CharField): Name of the tag. // Názov značky.
- `description` (TextField): Description of the tag. // Popis značky.

### Category
- `id` (IntegerField): Primary key. // Primárny kľúč.
- `name` (CharField): Name of the category. // Názov kategórie.
- `description` (TextField): Description of the category. // Popis kategórie.

## Media:
### Image
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
# WPAczsk
World Pheasant Association Czech Republic and Slovakia

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
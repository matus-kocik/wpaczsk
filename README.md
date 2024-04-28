# wpaczsk
World Pheasant Association Czech Republic and Slovakia

Databázový Model:

1. Role
   id
   name
2. User:
   id
   role_id
   first_name
   last_name
   user_name
   email
   password
   profile_picture
   mobile_phone
   address
   city
   country
4. Species
   id
   latin_name
   czech_name
   slovak_name
   conservation_status
   habitat
   average_lifespan
   description
   images
   url_video
6. Subspecies
   id
   species_id
   latin_name
   czech_name
   slovak_name
   conservation_status
   habitat
   average_lifespan
   description
   images
   url_video
8. breeding_record
   id
   breeder_id
   subspecies_id
   year
   number_of_males
   number_of_females
   number_of_species
   total_offsprings
   notes
9. event
   id
   name
   date_from
   date_to
   url
   location
   description
10. articels
   id
   title
   pdf_file
   publication_date
   author

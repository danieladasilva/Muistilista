# Muistilista

## Kuvaus

Muistilista-sovellus on tarkoitettu päivittäisten askareiden ja menojen hallintaan. Sovellukseen kirjaudutaan omalla käyttäjätunnuksella ja salasanalla. Sovelluksessa on mahdollista järjestellä omat muistettavat askareet omiin ryhmiinsä (syntymäpäivät, laskut, työasiat, opiskelu jne.). Käyttäjä pystyy itse lisäämään ja poistamaan ryhmiä. Sovellus mahdollistaa myös askareiden/muistilappujen järjestämisen tärkeysasteensa mukaan.

## Toiminnot

  - Rekisteröityminen käyttäjäksi omalla uniikilla käyttäjätunnuksella ja salasanalla (uniikki käyttäjätunnus puuttuu)
  - Kirjautuminen sisään sovellukseen/ulos sovelluksesta (toteutettu)
  - Tehtävien lisääminen, listaaminen, muokkaaminen ja poistaminen (muokkaaminen puuttuu vielä)
  	- Käyttäjä pystyy nimeämään tehtävän, merkitsemään tehtävän tehdyksi sekä luokittelemaan tehtävän haluamaansa ryhmään (toteutettu)
  - Ryhmien lisääminen ja poistaminen (poistaminen puuttuu vielä)
  	- Käyttäjä pystyy lisäämään ja poistamaan ryhmiä.
  - Sovellus näyttää käyttäjälle tilastotietoa
  	- Käyttäjä pystyy listaamaan kaikki tekemättömät tehtävänsä
    
	
## Linkkejä

#### **HEROKU**

#### [Linkki herokuun](https://tsoha-muistilista.herokuapp.com/)
	Testitunnukset: 
		käyttäjänimi: mikko
		salasana: mallikas


#### **TIETOKANTA**

#### [Linkki tietokantakaavioon ja CREATE TABLE -lauseisiin](https://github.com/danieladasilva/Muistilista/blob/master/documentation/dbschema.md)



#### **KÄYTTÖTAPAUKSET**

#### [Linkki käyttötapauksiin](https://github.com/danieladasilva/Muistilista/blob/master/documentation/stories.md)


## Asennusohjeet

1) Asenna Python ja sqlite3
2) Lataa projektin zip-tiedosto
3) Pura paketti
4) Luo virtuaaliympäristö komennolla python3 -m venv venv
5) Aktivoi sen jälkeen virtuaaliympäristö komennolla source venv/bin/activate
6) Päivitä pip komennolla pip install --upgrade pip
7) Asenna riippuvuudet komennolla pip install -r requirements.txt
8) Käynnistä sovellus komennolla python3 run.py
9) Mene selaimella osoitteeseen http://localhost:5000

-- Crear una taula per a emmagatzemar imatges
CREATE TABLE images(
    name TEXT PRIMARY KEY, -- Nom únic de la imatge
    size TEXT, -- Mida de la imatge
    date DATE -- Data en què es va crear la imatge
);

library(questionr)
install.packages('questionr')

column_names = c("Comptes", "Duree_credit", "Historique_credit", "Objet_credit", "Montant_credit", "Epargne",
    "Anciennete_emploi", "taux_effort", "Situation_familiale", "Garanties", "Anciennete_domicile", "Biens", "Age",
    "Autres_credits", "Statut_domicile", "Nb_credits", "Type_emploi", "Nb_pers_charge", "Telephone", "Etranger", "Cible")


df= read.table("data/credit.txt", col.names = column_names)

data_100 = data = read.table("data/credit.txt", nrows = 100, col.names = column_names)

head(df)

summary(df)

#irec()


## Recodage de data$Comptes en data$Comptes_rec
#data$Comptes_rec <- as.character(data$Comptes)
#data$Comptes_rec[data$Comptes == "A11"] <- "'CC < 0Euros'"
#data$Comptes_rec[data$Comptes == "A12"] <- "'0euros <= CC < 200Euros'"
#data$Comptes_rec[data$Comptes == "A13"] <- "'CC > 200Euros'"
#data$Comptes_rec[data$Comptes == "A14"] <- "'Pas de compte'"


#logistic regression

y =

smp_size <- floor(0.75 * nrow(df))
smp_size <- sample(seq_len(nrow(df)), size = smp_size)
smp_size

train <- df[smp_size,]
dim(train)

test <- df[-smp_size,]
dim(test)

x_train <- subset(X, select = -Cible)
head(x_train)

dim(x_train)

y_train <- train$Cible
y_train


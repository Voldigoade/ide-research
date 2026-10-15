# Méthode et incertitude

## Date et méthode de travail

L'état est vérifié au 15 octobre 2026. L'audit reprend le balayage de marché antérieur et les sources déjà collectées; il ne prétend pas repartir de zéro. Les versions et changements 2026 sont contrôlés dans les notes officielles listées par produit et dans le registre structuré.

La capacité documentée établit ce que le fournisseur prend en charge. Elle ne prouve ni qualité réelle, ni vitesse, ni sécurité indépendante. Les retours Reddit, Hacker News et GitHub Issues servent à repérer des frictions et migrations; ils ne représentent pas une population aléatoire.

## Échelle de notes

Chaque candidat reçoit une plage de 1 à 10 et une confiance des preuves pour chaque critère noté. Le modèle couvre 27 critères, dont les OS, l’UX, le prix et le verrouillage. Les duels comparent les 23 dimensions demandées; Docker et Dev Containers sont regroupés sous conteneurs.

- 9-10: couverture forte et intégrée, corroborée dans la documentation actuelle.
- 7-8: utilisable avec des limites ou dépendances visibles.
- 5-6: couverture partielle, configuration importante ou preuves faibles.
- 3-4: lacunes substantielles pour le workflow décrit.
- 1-2: absent ou incompatible.

Les deux nombres sont les bornes de jugement plausibles. Ils ne constituent ni intervalle de confiance statistique ni mesure contrôlée. Les notes de performance sont larges en l'absence de benchmark comparable.

## Modèle

Le modèle équilibré donne 55% au stack et 45% au workflow. Les scénarios spécialisés déplacent ce partage : Rust/Tauri 75% stack, web 65%, Python 68%, agents IA 15%, confidentialité 30%, remote 38% et profils OS 40%. La composition est aussi explicite: Rust/Tauri dominant attribue 55% du travail à Rust et 25% à Tauri. Les poids sont dans data/scenarios.json. Chaque poids de scénario est public et modifiable dans `data/scenarios.json`.

Les dimensions transversales d'un scénario sont renormalisées avant agrégation. Le score de chaque environnement conserve ses bornes. Le score médian prend le milieu de chaque intervalle. Le comparateur montre les plages; la page ne présente pas de décimales artificiellement précises.

## Sensibilité

Le script `scripts/analyze.py` utilise une graine fixée. Les notes à haute confiance sont échantillonnées autour du milieu; celles à confiance moyenne sont uniformes; celles à faible confiance tirent une distribution triangulaire à mode optimiste ou pessimiste choisi au hasard, dans les bornes de la note. Pour l'analyse des poids, il perturbe les poids de stack et les poids transversaux de +/-20%, puis les normalise. Trois résultats séparés sont produits: poids seuls, notes seules, notes et poids combinés. Le tableau affiche rang médian, plages de score p10-p90 et fréquence de première place arrondie au pourcent.

Ce calcul examine la stabilité interne d'un jugement éditorial. Il ne mesure pas la probabilité réelle de gagner sur le marché ni l'incertitude statistique d'un utilisateur. Les fréquences changeront si les notes, les intervalles, la graine ou la plage de poids changent.

## Performance

- **MESURÉ :** aucun benchmark entre IDEs n'a été réalisé. JetBrains publie cinq essais WSL IJent contre 9P sur IDEA Ultimate et Spring Framework; c'est une mesure fournisseur de son architecture, pas une comparaison de produits.
- **CORROBORÉ :** la documentation décrit architectures, LSP, indexation, remote et debugging; cela établit les mécanismes, pas la vitesse relative.
- **TÉMOIGNAGES RÉCURRENTS :** retours d'utilisateurs et issues publiques décrivent démarrage, mémoire, charge CPU, WSL et gros dépôts. Les échantillons sont biaisés et non dénombrés.
- **INFERENCE :** les éditeurs natifs peuvent avoir moins de surcharge de rendu qu'une application Electron, mais les language servers, extensions et indexations dominent parfois. Aucun score précis ne découle de cette seule architecture.

## Licence et coût

Les prix sont volatils et parfois régionaux. Le rapport donne des catégories et liens vers les plans officiels, pas un devis. Distinguer usage commercial, licence IDE, licence d'extension, service IA et coût de modèle.

from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .views import RegisterView,verify_otp
from DuramaProject.view import Panier_views,ProduitVariableImage,Etiquette_views,ProduitVariableAttribut_views,ProduitIlmage_views,ProduitVariable_views,TypeAttribut_views,subCategorie_views,Attribut_views,AvisProduit_views,categorie_views,Commande_view,Etiquette_views,PanierItem_views,Produit_views


urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # Obtenir le token
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'), # Rafraîchir le token
    path('register/', RegisterView.as_view(), name='register'),
    path("jwt/create/",TokenObtainPairView.as_view(),name="jwt-create"),
    path('verify_otp/', verify_otp, name='verification otp'),
    #Categorie
    path('creer-categorie/',categorie_views.createCategorie,name="creer_une_categorie"),
    path('changer-categorie/<int:categorie_id>/',categorie_views.changeCategorie,name="changer_categorie"),
    path('supprimer-categorie/<int:categorie_id>/',categorie_views.SupprimerCategorie,name="supprimer_une_categorie"),
    path('tous-categorie/',categorie_views.TousLesCategories,name="tous_les_categories"),
    path('details-categorie/<int:pk>/',categorie_views.DetailCategorie,name="detail_une_categorie"),
    #SubCategorie
    path('tous-les-souscategorie/',subCategorie_views.liste_souscategories,name="liste_des_sous_categories"),
    path('sous-categorie-par-categorie/<int:categorie_id>/',subCategorie_views.souscategories_par_categorie,name="sous_categorie_par_categorie"),
    path('details-sous-categorie/<int:categorie_id>/',subCategorie_views.detail_souscategorie,name="details_sous_categorie"),
    path('creer-sous-categorie/<int:categorie_id>/',subCategorie_views.creer_souscategorie,name="creer_une_sous_categorie"),
    path('modifier-sous-categorie/<int:souscategorie_id>/',subCategorie_views.modifier_souscategorie,name="modifier_sous_categorie"),
    path('supprimer-sous-categorie/<int:souscategorie_id>/',subCategorie_views.supprimer_souscategorie,name="supprimer_sous_categorie"),
    #TypeAttribut
    path('faire-type-attribut/',TypeAttribut_views.faireUnTypeAttribut,name="faire_un_type_attribut"),
    path('tous-type-attribut/',TypeAttribut_views.VoirTousTypeAttribut,name="voir_tous_les_types_attributs"),
    path('details-attribut/<int:pk>/',TypeAttribut_views.detailUnTypeAttribut,name="details_type_attribut"),
    path('changer-type-attribut/<int:pk>/',TypeAttribut_views.changerTypeAttribut,name="changer_type_attribut"),
    path('supprimer-un-type-attribut/<int:pk>/',TypeAttribut_views.SupprimerUnTypeAttribut,name="supprimer_un_type_attribut"),
    #Attribut
    path('creer-attribut/<int:typeAttribut>/',Attribut_views.creerAttribut,name="creer_attribut"),
    path('attributs-par-typeAtrributs/<int:typeAttribut_id>/',Attribut_views.TousLesAttribut,name="attribut_par_type_attribut"),
    path('details-attribut/<int:pk>/',Attribut_views.DetailsAttribut,name="Details_attribut"),
    path('changer-attribut/<int:pk>/',Attribut_views.changerUnAttribut,name="changer-un-attribut"),
    path('supprimer-attribut/<int:pk>/',Attribut_views.DeleteAttribut,name="supprimer_un_attribut"),
    #Etiquette
    path('creer-etiquette/',Etiquette_views.creerAttribut,name="creer_etiquette"),
    path('tous-les-etiquettes/',Etiquette_views.TousEtiquette,name="tous_les_etiquette"),
    path('details-etiquet/<int:pk>/',Etiquette_views.detailEtiquette,name="details_etiquette"),
    #Produits
    path('produits/', Produit_views.liste_produits, name="liste_produits"),
    path('produits-aleatoires/', Produit_views.TousLesProduitsAleatoirement, name="produits_aleatoires"),
    path('produits/<int:produit_id>/', Produit_views.detail_produit, name="detail_produit"),
    path('creer-produit/', Produit_views.creer_produit, name="creer_produit"),
    path('modifier-produit/<int:produit_id>/', Produit_views.modifier_produit, name="modifier_produit"),
    path('supprimer-produit/<int:produit_id>/', Produit_views.supprimer_produit, name="supprimer_produit"),
    path('produits-par-categorie/<int:categorie_id>/', Produit_views.produits_par_categorie, name="produits_par_categorie"),
    path('produits-par-souscategorie/<int:souscategorie_id>/', Produit_views.produits_par_souscategorie, name="produits_par_souscategorie"),
    path('produits-par-etiquette/<int:etiquette_id>/', Produit_views.produits_par_etiquette, name="produits_par_etiquette"),
    
    # Images de produits
    path('images/', ProduitIlmage_views.liste_images, name="liste_images"),
    path('images-par-produit/<int:produit_id>/',  ProduitIlmage_views.images_par_produit, name="images_par_produit"),
    path('ajouter-image/<int:produit_id>/',  ProduitIlmage_views.ajouter_image, name="ajouter_image"),
    path('details-image/<int:image_id>/',  ProduitIlmage_views.details_image, name="details_image"),
    path('supprimer-image/<int:image_id>/',  ProduitIlmage_views.supprimer_image, name="supprimer_image"),
    
    # Variantes de produits
    path('variantes/', ProduitVariable_views.liste_variantes, name="liste_variantes"),
    path('variantes-par-produit/<int:produit_id>/', ProduitVariable_views.variantes_par_produit, name="variantes_par_produit"),
    path('ajouter-variante/<int:produit_id>/', ProduitVariable_views.ajouter_variante, name="ajouter_variante"),
    path('details-variante/<int:variante_id>/', ProduitVariable_views.details_variante, name="details_variante"),
    path('modifier-variante/<int:variante_id>/', ProduitVariable_views.modifier_variante, name="modifier_variante"),
    path('supprimer-variante/<int:variante_id>/', ProduitVariable_views.supprimer_variante, name="supprimer_variante"),
    
    # Associations ProduitVariable <-> Attribut
    path('liens/', ProduitVariableAttribut_views.liste_produit_variable_attributs, name='liste_produit_variable_attributs'),
    path('ajouter-lien/', ProduitVariableAttribut_views.ajouter_produit_variable_attribut, name='ajouter_produit_variable_attribut'),
    path('variantes/<int:produit_variable_id>/attributs/', ProduitVariableAttribut_views.attributs_par_variante, name='attributs_par_variante'),
    path('attributs/<int:attribut_id>/variantes/', ProduitVariableAttribut_views.variantes_par_attribut, name='variantes_par_attribut'),
    path('supprimer-lien/<int:lien_id>/', ProduitVariableAttribut_views.supprimer_produit_variable_attribut, name='supprimer_produit_variable_attribut'),
    
        
    # IMAGES DE VARIANTES 
    
    path('variante-images/', ProduitVariableImage.liste_variante_images, name='liste_variante_images'),
    path('variante-images/<int:produit_variable_id>/', ProduitVariableImage.images_par_variante, name='images_par_variante'),
    path('variante-images/<int:produit_variable_id>/ajouter/', ProduitVariableImage.ajouter_variante_image, name='ajouter_variante_image'),
    path('variante-image/<int:image_id>/', ProduitVariableImage.details_variante_image, name='details_variante_image'),
    path('variante-image/<int:image_id>/supprimer/', ProduitVariableImage.supprimer_variante_image, name='supprimer_variante_image'),
    
    #Avis Produit
    path('tous-avis/',AvisProduit_views.tousAvis,name="tous_les_avis"),
    path('avis-par-produit/<int:produit_id>/',AvisProduit_views.AvisSurUnProduit,name="avis_sur_un_produit"),
    path('faire-avis-sur-un-produit/',AvisProduit_views.faireAvis,name="faire_un_avis_sur_un_produit"),
    path('supprimer-avis-produit/<int:produit_id>/',AvisProduit_views.deleteAvisProduit,name="supprimer_avis_produit"),
    path('details-avis-produit/<int:produit_id>/',AvisProduit_views.detailAvisSurProduit,name="details_avis_produit"),
    path('modifier-avis-produit/<int:produit_id>/',AvisProduit_views.modifierAvisProduit,name="modifier_avis_produits"),
    #Panier
    path('paniers/', Panier_views.liste_paniers, name='liste_paniers'),
    path('paniers/creer/', Panier_views.creer_panier, name='creer_panier'),
    path('paniers/<int:pk>/', Panier_views.panier_detail, name='panier_detail'),
    #PanierItem
    path('panier/items/', PanierItem_views.panier_items, name='panier_items'),
    path('panier/items/<int:pk>/', PanierItem_views.panier_item_detail, name='panier_item_detail'),
    #Commande
    path('commande/faire/', Commande_view.faire_une_commande, name='faire_une_commande'),
    path('commandes/', Commande_view.tous_les_commandes, name='tous_les_commandes'),
    path('commandes/user/<int:user_id>/', Commande_view.commandeParUser, name='commande_par_user'),
    path('commande/modifier/<int:pk>/', Commande_view.changerUneCommande, name='changer_une_commande'),
    
    
    
]
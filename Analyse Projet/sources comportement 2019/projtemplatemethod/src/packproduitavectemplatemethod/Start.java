package packproduitavectemplatemethod;

import packproduitsanstemplatemethod.Produit;
import packproduitsanstemplatemethod.ProduitAlimentaire;
import packproduitsanstemplatemethod.ProduitOrdinaire;

public class Start 
{
	public static void main(String[] args) 
	{
		Produit p1 = new ProduitAlimentaire("Nutella",4.0);
		System.out.println(p1);
		
		Produit p2 = new ProduitOrdinaire("DVD Harry Potter 7",20.0);
		System.out.println(p2);
	}
}


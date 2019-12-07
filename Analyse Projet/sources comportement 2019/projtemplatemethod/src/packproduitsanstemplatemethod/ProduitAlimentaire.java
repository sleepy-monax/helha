package packproduitsanstemplatemethod;
public class ProduitAlimentaire extends Produit	 
{
	public ProduitAlimentaire(String libelle, double prixHtva) 
	{	super(libelle, prixHtva);		}

	
	@Override								 
	public double getPrixTvac() 			 
	{										 
											 
		return getPrixHtva() * (1+0.06);	
	}
}

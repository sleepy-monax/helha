package packproduitsanstemplatemethod;
public class ProduitOrdinaire extends Produit 
{
	public ProduitOrdinaire(String libelle, double prixHtva) 
	{	super(libelle, prixHtva);				}

	//@Override
	public double getPrixTvac() 
	{	return getPrixHtva() * (1+0.21) + 2.;	}
}

package packproduitavectemplatemethod;

public class ProduitOrdinaire extends Produit 
{
	public ProduitOrdinaire(String libelle, double prixHtva) 
	{	super(libelle, prixHtva);				}


	@Override
	protected double calculerMontantTva() 
	{	return this.getPrixHtva()*0.21 + 2.;	}

}

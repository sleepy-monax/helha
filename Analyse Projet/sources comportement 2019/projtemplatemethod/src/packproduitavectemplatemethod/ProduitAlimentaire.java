package packproduitavectemplatemethod;

public class ProduitAlimentaire extends Produit 
{

	public ProduitAlimentaire(String libelle, double prixHtva) 
	{	super(libelle, prixHtva);		}


	@Override
	protected double calculerMontantTva() 
	{	return this.getPrixHtva()*0.06;	}

}

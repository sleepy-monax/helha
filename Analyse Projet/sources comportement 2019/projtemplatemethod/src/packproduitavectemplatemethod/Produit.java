package packproduitavectemplatemethod;
public abstract class Produit 
{	
	
	private String libelle;
	private double prixHtva;
	
	
	public Produit(String libelle, double prixHtva) 
	{
		this.libelle = libelle;
		this.prixHtva = prixHtva;
	}
	
	
	public String toString() 
	{
		return "Libellé : "+libelle+"\nPrix HTVA : "+prixHtva+
			"\nPrix TVAC : "+this.getPrixTvac();
	}

	
	public double getPrixHtva() 
	{	return prixHtva;	}
	
	public double getPrixTvac() 
	{	return prixHtva + calculerMontantTva();	}
	
	protected abstract double calculerMontantTva();
	

}

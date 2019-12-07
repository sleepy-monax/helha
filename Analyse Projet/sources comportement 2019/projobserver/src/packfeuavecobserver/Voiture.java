package packfeuavecobserver;

import packfeuavecobserver.Feu.Couleur;


public class Voiture implements Observer
{
	private String numPlaque;

	public Voiture(String numPlaque)
	{	this.numPlaque = numPlaque;						}


	public void demarrer()
	{	System.out.println(numPlaque + " roule ");		}

	public void sarreter()
	{	System.out.println(numPlaque + " s'arr�te");	}

	@Override
	public void actualise(Observable o)
	{
		if (((Feu)o).getCouleur() == Couleur.VERT)
		{	demarrer();
			// OU retirer de la liste en fonction de condition(s)
		}

	}

	public String getNumPlaque()
	{	return numPlaque;								}

	public String toString()
	{	return "Voiture : " + numPlaque;				}
}

package packfeuavecobserver;

import java.util.ArrayList;
import java.util.List;

public abstract class Observable		 
{
	
	private List<Observer> listeObservers;
	

	public Observable() 
	{	listeObservers = new ArrayList<Observer>();	}
	

	public void ajoute(Observer o) 
	{	listeObservers.add(o);						}
	
	// Clone de la liste afin de pouvoir retirer des éléments de la liste d'observers tout en pouvant la parcourir
	private List<Observer> cloneListeObservers()
	{
		List<Observer> copie = new ArrayList<Observer>();
		copie.addAll(listeObservers);
		return copie;
	}
	


	public void affichageListeObservers()
	{	
		for (Observer o : listeObservers)
		{	System.out.print(((Voiture)o).getNumPlaque() + " ");	}
	}
	
	
	public void notifie() 
	{	
		List<Observer> copie = cloneListeObservers();
			
		for (Observer o : copie)
		{	o.actualise(this);
			listeObservers.remove(o);
		}	
	}
}
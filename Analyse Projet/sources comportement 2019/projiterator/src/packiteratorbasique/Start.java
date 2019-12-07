package packiteratorbasique;
public class Start 
{
	public static void main(String[] args) 
	{
		Agenda agenda = new Agenda();
		
		Personne p1 = new Personne("Winch","Largo");
		Personne p2 = new Personne("Olivier","Génial");
		Personne p3 = new Personne("Vaillant","Michel");
		Personne p4 = new Personne("Castel","Eric");
		Personne p5 = new Personne("Lagaffe","Gaston");
				
		
		try { agenda.ajouter(p1);		} 
		catch (ElementDejaPresent e) 
				{ e.printStackTrace();	}
	
		try { agenda.ajouter(p2);		} 
		catch (ElementDejaPresent e) 
				{ e.printStackTrace();	}
		
		try { agenda.ajouter(p3);		} 
		catch (ElementDejaPresent e) 
				{ e.printStackTrace();	}
		
		try   {	agenda.ajouter(p4);		} 
		// affiche si la personne est déjà présente
		catch (ElementDejaPresent e)		
				{ e.printStackTrace();	}									
		
		
		try   {	agenda.ajouter(p4);		}		  
		catch (ElementDejaPresent e)			 
				{ System.out.println("Existe dejà : " + e.getMessage());	}
		
		try { agenda.ajouter(p5);		} 
		catch (ElementDejaPresent e) 
				{ e.printStackTrace();	}
				
	
		IteratorPersonne it = agenda.creerIterateur();
			
		Personne p; 
					
		// DEBUT -> FIN
		while ((p = it.item()) != null)						 
		{
			System.out.print(it.getIndex() + " : ");	// affiche l'index
			System.out.println(p.toString());			// affiche l'élément en cours et ...
			it.next();					    			// ... passe au suivant
		}
		
			
		// FIN -> DEBUT
		System.out.println(it.indexDernier() + "\n");
			
		while ((p = it.item()) != null)							 
		{
			System.out.print(it.getIndex() + " : ");	// affiche l'index
			System.out.println(p.toString());	        // affiche l'élément en cours et ... 
			it.preview(); 						        // ... passe au précédent
		}
			
	}
}
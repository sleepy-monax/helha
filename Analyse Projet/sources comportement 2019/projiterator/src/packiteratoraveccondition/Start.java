	package packiteratoraveccondition;
public class Start 
{
	public static void main(String[] args) 
	{
		// Création d'un Agenda
		Agenda agenda = new Agenda();
		
		// Création de 6 personnes
		Personne p1 = new Personne("Winch","Largo");
		Personne p2 = new Personne("Olivier","Génial");
		Personne p3 = new Personne("Vaillant","Michel");
		Personne p4 = new Personne("Castel","Eric");
		Personne p5 = new Personne("Lagaffe","Gaston");
		
		// Essaie d'ajouter des personnes		
		try { agenda.ajouter(p1);		} 
		catch (ElementDejaPresent e) 
		{ e.printStackTrace();	}

		try { agenda.ajouter(p2);		} 
		catch (ElementDejaPresent e) 
				{ e.printStackTrace();	}
		
		try { agenda.ajouter(p3);		} 
		catch (ElementDejaPresent e) 
				{ e.printStackTrace();	}
		
		try { agenda.ajouter(p4);		} 
		catch (ElementDejaPresent e) 
				{ e.printStackTrace();	}
		
		try { agenda.ajouter(p5);		} 
		catch (ElementDejaPresent e) 
				{ e.printStackTrace();	}


		
		IteratorPersonne it = agenda.rechercheAlpha("Lemaitre");
		
		Personne p;
		while ((p = it.item()) != null) 
		{
			System.out.println(p.toString());
			it.next();
		}
	}
}
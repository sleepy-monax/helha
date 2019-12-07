package packjeuavecstate; 
public class TestState 	
{
	public static void main(String[] args) 
	{

		Utilisateur user1 = new Utilisateur("toto","blague");
		Utilisateur user2 = new Utilisateur("astérix","obélix");
		Utilisateur user3 = new Utilisateur("tintin","milou");
		Utilisateur user4 = new Utilisateur("spirou","fantasio");
		Utilisateur user5 = new Utilisateur("laurel","hardy");
		Utilisateur user6 = new Utilisateur("morane","ballantine");
		
		JeuVideo jeu = new JeuVideo("Le meilleur de la BD");
		
		System.out.println("****************Jeu en développement");
		jeu.ajouterUtilisateur(user1);
		jeu.ajouterUtilisateur(user2);
		jeu.ajouterUtilisateur(user3);
		jeu.ajouterUtilisateur(user4);
		jeu.ajouterUtilisateur(user5);
		jeu.ajouterUtilisateur(user6);
		System.out.println(jeu + " : Liste vide : pas d'ajout");		
		
		
		
		jeu.retirerUtilisateur(user5);
		jeu.retirerUtilisateur(user2);
		System.out.println(jeu + " : Liste vide : pas de suppression 1 à 1 <Liste vide>");		
		
		jeu.efface();
		System.out.println(jeu + " : Liste vide : pas de suppression intégrale");		
		
		
		jeu.etatSuivant();
		System.out.println("\n\n********************Jeu en bêta");
		

		jeu.ajouterUtilisateur(user1);
		jeu.ajouterUtilisateur(user2);
		jeu.ajouterUtilisateur(user3);
		jeu.ajouterUtilisateur(user4);
		jeu.ajouterUtilisateur(user5);
		jeu.ajouterUtilisateur(user6);
		System.out.println(jeu);		
		
		jeu.retirerUtilisateur(user5);
		jeu.retirerUtilisateur(user2);
		System.out.println("\n" + jeu + "\n --> tous les joueurs sont là : suppression impossible");		
		
		jeu.efface();
		System.out.println("\n" + jeu + "\n --> Liste complète des utilisateurs effacée");		
		
		
		jeu.etatSuivant();
		System.out.println("\n\n********************Jeu définitif");
		
		jeu.ajouterUtilisateur(user1);
		jeu.ajouterUtilisateur(user2);
		jeu.ajouterUtilisateur(user3);
		jeu.ajouterUtilisateur(user4);
		jeu.ajouterUtilisateur(user5);
		jeu.ajouterUtilisateur(user6);
		System.out.println(jeu);		
		
		jeu.retirerUtilisateur(user5);
		jeu.retirerUtilisateur(user2);
		System.out.println("\n" + jeu + "\n --> suppression utilisateurs 2 et 5");		
		

		jeu.efface();
		System.out.println("\n" + jeu + "\n --> Liste complète des utilisateurs effacée");		
		
		jeu.etatSuivant();
	}
}

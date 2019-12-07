package packjeuavecstate;

public class JeuBeta extends EtatJeuVideo	 
{
	public JeuBeta(JeuVideo jeu) 
	{	super(jeu);					}

	@Override 
	public void ajouterUtilisateur(Utilisateur user) 	
	{	this.getJeu().getUtilisateurs().add(user);	}

	@Override 
	public void retirerUtilisateur(Utilisateur user){} 
		
	@Override 
	public void efface() 
	{	this.getJeu().getUtilisateurs().clear();			}	
																
	@Override 
	public EtatJeuVideo etatSuivant() 
	{	return new JeuDefinitif(this.getJeu());				}	
}
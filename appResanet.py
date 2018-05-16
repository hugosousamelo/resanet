#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask import *
from modeles import modeleResanet
from technique import datesResanet


app = Flask( __name__ )
app.secret_key = 'resanet'


@app.route( '/' , methods = [ 'GET' ] )
def index() :
	return render_template( 'vueAccueil.html' )

@app.route( '/usager/session/choisir' , methods = [ 'GET' ] )
def choisirSessionUsager() :
	return render_template( 'vueConnexionUsager.html' , carteBloquee = False , echecConnexion = False , saisieIncomplete = False )

@app.route( '/usager/seConnecter' , methods = [ 'POST' ] )
def seConnecterUsager() :
	numeroCarte = request.form[ 'numeroCarte' ]
	mdp = request.form[ 'mdp' ]

	if numeroCarte != '' and mdp != '' :
		usager = modeleResanet.seConnecterUsager( numeroCarte , mdp )
		if len(usager) != 0 :
			if usager[ 'activee' ] == True :
				session[ 'numeroCarte' ] = usager[ 'numeroCarte' ]
				session[ 'nom' ] = usager[ 'nom' ]
				session[ 'prenom' ] = usager[ 'prenom' ]
				session[ 'mdp' ] = mdp
				
				return redirect( '/usager/reservations/lister' )
				
			else :
				return render_template('vueConnexionUsager.html', carteBloquee = True , echecConnexion = False , saisieIncomplete = False )
		else :
			return render_template('vueConnexionUsager.html', carteBloquee = False , echecConnexion = True , saisieIncomplete = False )
	else :
		return render_template('vueConnexionUsager.html', carteBloquee = False , echecConnexion = False , saisieIncomplete = True)


@app.route( '/usager/seDeconnecter' , methods = [ 'GET' ] )
def seDeconnecterUsager() :
	session.pop( 'numeroCarte' , None )
	session.pop( 'nom' , None )
	session.pop( 'prenom' , None )
	return redirect( '/' )


@app.route( '/usager/reservations/lister' , methods = [ 'GET' ] )
def listerReservations() :
	tarifRepas = modeleResanet.getTarifRepas( session[ 'numeroCarte' ] )
	
	soldeCarte = modeleResanet.getSolde( session[ 'numeroCarte' ] )
	
	solde = '%.2f' % ( soldeCarte , )

	aujourdhui = datesResanet.getDateAujourdhuiISO()

	datesPeriodeISO = datesResanet.getDatesPeriodeCouranteISO()
	
	datesResas = modeleResanet.getReservationsCarte( session[ 'numeroCarte' ] , datesPeriodeISO[ 0 ] , datesPeriodeISO[ -1 ] )
	
	ferie = modeleResanet.getFerie()
	dates = []
				
	for uneDateISO in datesPeriodeISO :
		uneDate = {}
		uneDate[ 'iso' ] = uneDateISO
		uneDate[ 'fr' ] = datesResanet.convertirDateISOversFR( uneDateISO )	
		
		if uneDateISO <= aujourdhui :
			uneDate[ 'verrouillee' ] = True
		else :
			uneDate[ 'verrouillee' ] = False

		if uneDateISO in datesResas :
			uneDate[ 'reservee' ] = True
		else :
			uneDate[ 'reservee' ] = False
			
		if soldeCarte < tarifRepas and uneDate[ 'reservee' ] == False :
			uneDate[ 'verrouillee' ] = True
			
			
		for i in ferie:
			if str(uneDateISO) == str(i[0]):
					uneDate[ 'verrouillee' ] = True
			
		
				
			
			
		dates.append( uneDate )
	
	if soldeCarte < tarifRepas :
		soldeInsuffisant = True
	else :
		soldeInsuffisant = False
		
	jour = ["Lundi","Mardi","Mercredi","Jeudi","Vendredi","Lundi","Mardi","Mercredi","Jeudi","Vendredi"]
	
	print dates	
	
	return render_template( 'vueListeReservations.html' , laSession = session , leSolde = solde , lesDates = dates , soldeInsuffisant = soldeInsuffisant, jour = jour )

	
@app.route( '/usager/reservations/annuler/<dateISO>' , methods = [ 'GET' ] )
def annulerReservation( dateISO ) :
	modeleResanet.annulerReservation( session[ 'numeroCarte' ] , dateISO )
	modeleResanet.crediterSolde( session[ 'numeroCarte' ] )
	return redirect( '/usager/reservations/lister' )
	
@app.route( '/usager/reservations/enregistrer/<dateISO>' , methods = [ 'GET' ] )
def enregistrerReservation( dateISO ) :
	modeleResanet.enregistrerReservation( session[ 'numeroCarte' ] , dateISO )
	modeleResanet.debiterSolde( session[ 'numeroCarte' ] )
	return redirect( '/usager/reservations/lister' )

@app.route( '/usager/mdp/modification/choisir' , methods = [ 'GET' ] )
def choisirModifierMdpUsager() :
	soldeCarte = modeleResanet.getSolde( session[ 'numeroCarte' ] )
	solde = '%.2f' % ( soldeCarte , )
	
	return render_template( 'vueModificationMdp.html' , laSession = session , leSolde = solde , modifMdp = '' )

@app.route( '/usager/mdp/modification/appliquer' , methods = [ 'POST' ] )
def modifierMdpUsager() :
	ancienMdp = request.form[ 'ancienMDP' ]
	nouveauMdp = request.form[ 'nouveauMDP' ]
	
	soldeCarte = modeleResanet.getSolde( session[ 'numeroCarte' ] )
	solde = '%.2f' % ( soldeCarte , )
	
	if ancienMdp != session[ 'mdp' ] or nouveauMdp == '' :
		return render_template( 'vueModificationMdp.html' , laSession = session , leSolde = solde , modifMdp = 'Nok' )
		
	else :
		modeleResanet.modifierMdpUsager( session[ 'numeroCarte' ] , nouveauMdp )
		session[ 'mdp' ] = nouveauMdp
		return render_template( 'vueModificationMdp.html' , laSession = session , leSolde = solde , modifMdp = 'Ok' )


@app.route( '/gestionnaire/session/choisir' , methods = [ 'GET' ] )
def choisirSessionGestionnaire():
	return render_template( 'vueConnexionGestionnaire.html' )
	
@app.route( '/gestionnaire/seConnecter' , methods = [ 'POST' ] )
def seConnecterGestionnaire() :
	login = request.form[ 'login' ]
	mdp = request.form[ 'mdp' ]

	if login != '' and mdp != '' :
		gestionnaire = modeleResanet.seConnecterGestionnaire( login , mdp )
		if len(gestionnaire) != 0 :
			session[ 'login' ] = gestionnaire[ 'login' ]
			session[ 'nom' ] = gestionnaire[ 'nom' ]
			session[ 'prenom' ] = gestionnaire[ 'prenom' ]
			session[ 'mdp' ] = mdp
				
			return redirect("/gestionnaire/personnels/avec/carte")
				
		else :
			return render_template('vueConnexionGestionnaire.html', echecConnexion = True , saisieIncomplete = False )
	else :
		return render_template('vueConnexionGestionnaire.html', echecConnexion = False , saisieIncomplete = True)

@app.route ( '/gestionnaire/personnels/avec/carte', methods = [ 'GET' ]  )
def gestionnairePersonnelsAvecCarte():
	avecCarte = modeleResanet.getPersonnelsAvecCarte()
	longeur = len(avecCarte)
	nom = []
	prenom = []
	nomService = []
	solde = []
	matricule = []
	activee = []
	numeroCarte = []
	
	for i in range(len(avecCarte)):
		nom.append(avecCarte[i]['nom'])
		prenom.append(avecCarte[i]['prenom'])
		nomService.append(avecCarte[i]['nomService'])
		solde.append(avecCarte[i]['solde'])
		matricule.append(str(avecCarte[i]['matricule']))
		activee.append(avecCarte[i]['activee'])
		numeroCarte.append(avecCarte[i]['numeroCarte'])
	
	return render_template( 'vuePersonnelAvecCarte.html', perso = longeur, leNom = nom, lePrenom = prenom, nomDuService = nomService, leSolde = solde, leMatricule = matricule, activee = activee, numCarte = numeroCarte)

@app.route ( '/gestionnaire/personnels/sans/carte', methods = [ 'GET' ]  )
def gestionnairePersonnelsSansCarte():
	sansCarte = modeleResanet.getPersonnelsSansCarte()
	longeur = len(sansCarte)
	nom = []
	prenom = []
	nomService = []
	matricule = []
	
	for i in range(len(sansCarte)):
		nom.append(sansCarte[i]['nom'])
		prenom.append(sansCarte[i]['prenom'])
		nomService.append(sansCarte[i]['nomService'])
		matricule.append(str(sansCarte[i]['matricule']))
	
	return render_template( 'vuePersonnelSansCarte.html', perso = longeur, leNom = nom, lePrenom = prenom, nomDuService = nomService, leMatricule = matricule)

@app.route( '/gestionnaire/seDeconnecter' , methods = [ 'GET' ] )
def seDeconnecterGestionnaire() :
	session.pop( 'login' , None )
	session.pop( 'nom' , None )
	session.pop( 'prenom' , None )
	return redirect( '/' )
	
@app.route('/gestionnaire/activeCarte' , methods = [ 'POST' ] )
def activerCarte():
	numCarte = request.form[ 'numeroCarte' ]
	modeleResanet.activerCarte( numCarte )
	return redirect("/gestionnaire/personnels/avec/carte")
		
@app.route('/gestionnaire/bloquerCarte' , methods = [ 'POST' ] )
def bloquerCarte():
	numCarte = request.form[ 'numeroCarte' ]
	modeleResanet.bloquerCarte( numCarte )
	return redirect("/gestionnaire/personnels/avec/carte")
		
@app.route('/gestionnaire/userMatricule' , methods = [ 'POST' ] )
def userMatricule():
	numCarte = request.form[ 'numeroCarte' ]
	return render_template('vueCrediterCarte.html', numCarte = numCarte )

@app.route('/gestionnaire/crediterCarte' , methods = [ 'POST'] )
def crediterCarte():
	numCarte = request.form[ 'numeroCarte' ]	
	montant = request.form[ 'montant' ]
	crediterCarte = modeleResanet.crediterCarte( numCarte, montant )
	return redirect("/gestionnaire/personnels/avec/carte")
	
	
@app.route('/gestionnaire/initPage' , methods = [ 'POST' ] )
def initPage():
	numCarte = request.form[ 'numeroCarte' ]
	initMDP = modeleResanet.reinitialiserMdp( numCarte )
	return redirect("/gestionnaire/personnels/avec/carte")
	
	
@app.route('/gestionnaire/historiqueCarte' , methods = [ 'POST' ] )
def historiqueCarte():
	numCarte = request.form[ 'numeroCarte' ]
	historique = modeleResanet.getHistoriqueReservationsCarte( numCarte )
	longueur = len(historique)
	return render_template('vueHistoriqueCarte.html', historique = historique,longueur = longueur, numCarte = numCarte)
		
@app.route('/gestionnaire/creerCompte' , methods = [ 'POST' ] )
def creerCompte():
	matricule = request.form[ 'matricule' ]
	modeleResanet.creerCarte(matricule)
	return redirect("/gestionnaire/personnels/sans/carte")
	
@app.route('/gestionnaire/avecDate' , methods = [ 'GET' ] )
def historique():
	avecCarte = modeleResanet.getPersonnelsAvecCarte()
	longeur = len(avecCarte)
	nom = []
	prenom = []
	nomService = []
	solde = []
	matricule = []
	activee = []
	numeroCarte = []

	
	for i in range(len(avecCarte)):
		nom.append(avecCarte[i]['nom'])
		prenom.append(avecCarte[i]['prenom'])
		nomService.append(avecCarte[i]['nomService'])
		solde.append(avecCarte[i]['solde'])
		matricule.append(str(avecCarte[i]['matricule']))
		activee.append(avecCarte[i]['activee'])
		numeroCarte.append(avecCarte[i]['numeroCarte'])
	
	return render_template( 'vueHistoriqueDate.html', perso = longeur, leNom = nom, lePrenom = prenom, nomDuService = nomService, leSolde = solde, leMatricule = matricule, numCarte = numeroCarte, date = 0, liste = 0 , longueur = 0)

@app.route('/gestionnaire/historiqueDate' , methods = [ 'POST' ] )
def historiqueDate():
	date = request.form[ 'dateHistorique' ]
	liste = modeleResanet.getReservationsDate(date)
	longueur = len(liste)
	
	avecCarte = modeleResanet.getPersonnelsAvecCarte()
	longeur = len(avecCarte)
	nom = []
	prenom = []
	nomService = []
	solde = []
	matricule = []
	activee = []
	numeroCarte = []
	
	for i in range(len(avecCarte)):
		nom.append(avecCarte[i]['nom'])
		prenom.append(avecCarte[i]['prenom'])
		nomService.append(avecCarte[i]['nomService'])
		matricule.append(str(avecCarte[i]['matricule']))
		numeroCarte.append(avecCarte[i]['numeroCarte'])
	return render_template('vueHistoriqueDate.html', perso = longeur, leNom = nom, lePrenom = prenom, nomDuService = nomService, leMatricule = matricule, liste = liste, longueur = longueur, date = date, numCarte = numeroCarte)

@app.route ( '/gestionnaire/historiquePourCarte', methods = [ 'GET' ]  )
def gestionnaireHistoriquePourCarte():
	avecCarte = modeleResanet.getPersonnelsAvecCarte()
	longeur = len(avecCarte)
	nom = []
	prenom = []
	nomService = []
	matricule = []
	numeroCarte = []
	
	for i in range(len(avecCarte)):
		nom.append(avecCarte[i]['nom'])
		prenom.append(avecCarte[i]['prenom'])
		nomService.append(avecCarte[i]['nomService'])
		matricule.append(str(avecCarte[i]['matricule']))
		numeroCarte.append(avecCarte[i]['numeroCarte'])
	
	return render_template( 'vueHistoriqueAvecCarte.html', perso = longeur, leNom = nom, lePrenom = prenom, nomDuService = nomService, leMatricule = matricule, numCarte = numeroCarte)

if __name__ == '__main__' :
	app.run( debug = True , host = '0.0.0.0' , port = 5000 )

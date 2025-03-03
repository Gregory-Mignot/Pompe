# Pompe
contrôle d'une pompe (moteur dc piloté par esc) par arduino et python via serial

➡️ Définir une consigne de vitesse
    1. Saisissez une valeur entre 0 et 100 dans le champ de saisie.
    2. Appuyez sur Entrée ou cliquez sur "Envoyer" pour envoyer la consigne à l'Arduino.
    3. Un message de confirmation indique la vitesse envoyée.
📌 Note : 0% correspond à l'arrêt de la pompe et 100% à sa vitesse maximale.
🛑 Arrêter la pompe
    • Cliquez sur le bouton "Arrêt Pompe" :
        ◦ La consigne est immédiatement mise à 0%.
        ◦ Un message indique que la pompe est arrêtée.
❌ Quitter l'application
    • Cliquez sur le bouton "STOP" pour :
        ◦ Arrêter définitivement la pompe.
        ◦ Fermer l'application.

🛠 3. Dépannage
❓ L'application ne se lance pas
    1. Vérifiez que Python est installé :
        ◦ Ouvrez une invite de commandes (Win + R, tapez cmd, appuyez sur Entrée).
        ◦ Tapez : python --version
        ◦ Si Python n'est pas installé, suivez le guide d'installation.
    2. Assurez-vous que l’Arduino est bien connecté :
        ◦ Vérifiez que le câble USB est bien branché.
        ◦ Si nécessaire, relancez l’application.
    3. Réinstallez la bibliothèque pyserial :
        ◦ Dans l'invite de commandes, tapez : pip install pyserial
🚨 Message "Aucun Arduino détecté"
    • Vérifiez que l’Arduino est bien branché et reconnu dans le Gestionnaire de périphériques.
    • Si besoin, réinstallez les pilotes CH340 si vous utilisez un clone Arduino.

💡 Astuce : Vous pouvez épingler le raccourci sur la barre des tâches pour un accès rapide.
🔧 Support : En cas de problème persistant, contactez Grégory Mignot au laboratoire Optimag, UFR Sciences et Techniques, UBO.  mignot@univ-brest.fr .
Fichiers sources sur le dépôt Github https://github.com/Gregory-Mignot/Pompe

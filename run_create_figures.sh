#! /bin/bash

if [ -z "$1" ]
  then
    echo "ERROR: Please provide the name of the location for the figures or 'ALL' to compute all."
else
    if [ "$1" = "ALL" ] || [ "$1" = "cucuta" ]; then
        echo 'Cucuta'
        # Cucuta
        # Transits Housing
        python figure_generation/scripts/transits_housing_plots.py reporte_norte_de_santander 30 colombia_cucuta

        # Movement Plots
        python figure_generation/scripts/movement_plots.py reporte_norte_de_santander 30 colombia_cucuta_comuna_*

        # Centrality
        python figure_generation/scripts/centrality_housing_plots.py reporte_norte_de_santander colombia_cucuta personalized_pagerank_centrality 45 500 2
        
        # Edgelist
        python figure_generation/scripts/edgelist_plots.py reporte_norte_de_santander colombia_cucuta 30 3        
    
    elif [ "$1" = "ALL" ] || [ "$1" = "palmira" ] 
        then
        echo 'Palmira'

        # Plamira
        # Transits Housing
        python figure_generation/scripts/transits_housing_plots.py reporte_palmira 30 colombia_palmira

        # Movement Plots
        python figure_generation/scripts/movement_plots.py reporte_palmira 30 colombia_palmira_comuna_*

        # Centrality
        python figure_generation/scripts/centrality_housing_plots.py reporte_palmira colombia_palmira pagerank_centrality 45 500 2.5

        # Edgelist
        python figure_generation/scripts/edgelist_plots.py reporte_palmira colombia_palmira 30 2.5

    elif [ "$1" = "ALL" ] || [ "$1" = "bogota" ] 
        then
        echo 'Bogotá'

        # Bogota
        # Transits Housing
        python figure_generation/scripts/transits_housing_plots.py reporte_bogota 30 colombia_bogota

        # Centrality
        python figure_generation/scripts/centrality_housing_plots.py reporte_bogota colombia_bogota personalized_pagerank_centrality 45 500 2.5

        # Edgelist
        python figure_generation/scripts/edgelist_plots.py reporte_bogota colombia_bogota 20 2.5
        
    elif [ "$1" = "ALL" ] || [ "$1" = "ibague" ] 
        then
        echo 'Ibague'
        # Transits Housing
        python figure_generation/scripts/transits_housing_plots.py reporte_tolima 30 colombia_ibague

        # Centrality
        python figure_generation/scripts/centrality_housing_plots.py reporte_tolima colombia_ibague pagerank_centrality 30 5000 2

        # Edgelist
        python figure_generation/scripts/edgelist_plots.py reporte_tolima colombia_ibague 30 2

    elif [ "$1" = "ALL" ] || [ "$1" = "armenia" ] 
        then
        echo 'Armenia'
        # Transits Housing
        python figure_generation/scripts/transits_housing_plots.py reporte_quindio 30 colombia_armenia

        # Centrality
        python figure_generation/scripts/centrality_housing_plots.py reporte_quindio colombia_armenia pagerank_centrality 30 5000 2

        # Edgelist
        python figure_generation/scripts/edgelist_plots.py reporte_quindio colombia_armenia 30 5

    elif [ "$1" = "ALL" ] || [ "$1" = "popayan" ] 
        then
        echo 'Popayán'
        # Transits Housing
        python figure_generation/scripts/transits_housing_plots.py reporte_popayan 30 colombia_popayan

        # Centrality
        python figure_generation/scripts/centrality_housing_plots.py reporte_popayan colombia_popayan pagerank_centrality 30 5000 2

        # Edgelist
        python figure_generation/scripts/edgelist_plots.py reporte_popayan colombia_popayan 30 2
        
    else
        echo "Parameter not foud"
        
    fi
fi

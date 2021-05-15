        	district_select = document.getElementById('district')
        	bloodbank_select = document.getElementById('name')
        	
        	district_select.onchange= function() {
        		district = district_select.value;
        		console.log(district)

        		fetch('blood_bank/' + district).then(function(response){
        			response.json().then(function(data){

        			
        				
        				optionHTML ='';
        				for (bloodbank of data.bb){
        					// console.log(bloodbank)
        					// console.log('heloo')

        					optionHTML += '<option value="' + bloodbank.id +'">' + bloodbank.name + '</option>'
        					// console.log(optionHTML)
        				}

        				bloodbank_select.innerHTML = optionHTML;
        			});
        		});
        	}	

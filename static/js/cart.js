        const addBtn = document.getElementById('add-btn')

        //document.cookie = "cart=0; path=/";

        console.log(document.cookie)

        // var cartArr

        if(!document.cookie.includes('productId')){
        	document.cookie = "productId=0; path=/";
        }

   //      function getCookie(name) {
			//   const value = `; ${document.cookie}`;
			//   const parts = value.split(`; ${name}=`);
			//   if (parts.length === 2) return parts.pop().split(';').shift();
			// }

			// console.log('cart cookie: ' + getCookie('cart'))

		function getIdProduct(item) {
			// productsId.push(item)
			// console.log(productsId)
			// document.cookie = "product=" + item + "; path=/";
			document.cookie = "productId=" + item + "; path=/";
		}

		function getQuantity(quantity, id) {
//		var x = document.getElementById("quantity").value;
            console.log('get quantity: ' + quantity)
            console.log('get id: ' + id)

            document.cookie = "quantityProductId=" + id + "; path=/";
            document.cookie = "quantity=" + quantity + "; path=/";


//            const productQuantity = {
//            quantity: x,
//            productId: y,
//            }
//
//        window.localStorage.setItem('productQuantity', JSON.stringify(productQuantity));


		}
        
//        https://gist.github.com/jansanchez/6694824

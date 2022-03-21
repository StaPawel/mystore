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
        
//        https://gist.github.com/jansanchez/6694824

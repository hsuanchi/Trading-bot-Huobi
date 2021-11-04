$('#run').on('click', ()=>{
  var account, api_key, secret_key, ammount, price;
  account = $('#account').val();
  api_key = $('#api_key').val();
  secret_key = $('#secret_key').val();
  ammount = $('#ammount').val();
  price = $('#price').val();
  eel.create_trade_bot(account, api_key, secret_key, ammount=ammount, price=price)
})

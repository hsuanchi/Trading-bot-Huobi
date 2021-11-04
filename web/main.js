$('#run').on('click', ()=>{
  var api_key, secret_key, ammount;
  api_key = $('#api_key').val();
  secret_key = $('#secret_key').val();
  ammount = $('#ammount').val();
  eel.run_trade_bot(api_key, secret_key, ammount=ammount)
})

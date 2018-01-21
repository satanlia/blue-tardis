var repl = new ReplitClient('api.repl.it', 80, 'ruby', token);
repl.connect().then(() =>
  repl.evaluate(
    'puts "hello worls"',
     { stdout: out => console.log(out) }
  );
});

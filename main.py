import app

debug = False

if debug:
    import cProfile
    cProfile.run("app.App().run()")
else:
    app.App().run()
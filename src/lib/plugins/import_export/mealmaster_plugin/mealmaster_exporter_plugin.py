from gourmet.plugin import ExporterPlugin
import gourmet.exporters.exporter as exporter
import mealmaster_exporter

MMF = _('MealMaster file')

class MealmasterExporterPlugin (ExporterPlugin):

    label = _('MealMaster Export')
    sublabel = _('Exporting recipes to MealMaster file %(file)s.')
    single_completed_string = _('Recipe saved as MealMaster file %(file)s')
    filetype_desc = MMF
    saveas_filters = [MMF,['text/mmf'],['*.mmf','*.MMF']]
    saveas_single_filters = [MMF,['text/html'],['']]

    def get_multiple_exporter (self, args):
        return exporter.ExporterMultirec(
            args['rd'],
            args['rv'],
            args['file'],
            one_file=True,
            ext='mmf',
            conv=args['conv'],
            progress_func=args['prog'],
            exporter=mealmaster_exporter.mealmaster_exporter)

    def do_single_export (self, args)    :
        return mealmaster_exporter.mealmaster_exporter(args['rd'],
                                                       args['rec'],
                                                       args['out'],
                                                       mult=args['mult'],
                                                       change_units=args['change_units'],
                                                       conv=args['conv'])

    def run_extra_prefs_dialog (self):
        pass
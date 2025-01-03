from ... import errors
from ..base import rules


class BhdBannedGroup(rules.BannedGroup):

    banned_groups = {
        '4K4U',
        'AOC',
        'C4K',
        'd3g',
        'EASports',
        'FGT',  # Unless no other encode is available.
        'MeGusta',
        'MezRips',
        'nikt0',
        'ProRes',
        'RARBG',
        'ReaLHD',
        'SasukeducK',
        'Sicario',
        'TEKNO3D',  # They have requested their torrents are not shared off site.
        'Telly',
        'tigole',
        'TOMMY',
        'WKS',
        'x0r',
        'YIFY',
    }

    def custom_check(self):
        # No iFT remuxes.
        if (
                self.is_group('iFT')
                and 'Remux' in self.release_name.source
        ):
            raise errors.BannedGroup('iFT', additional_info='Remuxes (at the request of iFT)')

        # No EVO encodes. WEB-DLs are fine.
        if (
                self.is_group('EVO')
                and (
                    'BluRay' in self.release_name.source
                    or 'WebRip' in self.release_name.source
                )
        ):
            raise errors.BannedGroup('EVO', additional_info='No encodes allowed, only WEB-DL')

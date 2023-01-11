#=========================================================================
# [AutoDelete - Telegram bot to delete messages after specific time]      
# Copyright (C) 2022 Arunkumar Shibu                       
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
#=========================================================================

import os

API_ID       = int(os.environ.get("API_ID", "22359038"))
API_HASH     = os.environ.get("API_HASH", "b3901895dc193c30c808ba4f1b550ed0")
BOT_TOKEN    = os.environ.get("BOT_TOKEN", "5630873709:AAHtEhH9rsZslFQw3dHngt37jjwkNdK16qc")
SESSION      = os.environ.get("SESSION", "AQAZZkkAdPnQgRuW6gwP7UiwIHj1Jb78FAnJf9Sk2Vi0IcBwHf5Cd46wDsavrBFyteObURHPb549cdQ28G3cOcTz4TEfKUgfsFsuTbhVuflrY6o7YfRB6r6WfytnfaNXFCJ-XExChLn70fVkgyTBZqoLUidmYD_UpxdgWatXDYwoabJc0QdA9hQ0BBp9fsJirsH0z5GcMLBIk2nt_dNPQxvS_WZNRMxI-9LjPxJUT4w9LlMmosrAfBELIlyjIX_vmGVAdRZYeQJ8U0GWZK6lkTlsc5PwUA-9WMPg9nHz2AxHkFr-cpDTJKfIuf2CbWFz9aXlTWGHeWVCyhIjj_-ACTqt4ASfSQAAAAFEMn5gAA")
TIME         = int(os.environ.get("TIME", 10))
CHATS        = [int(cht) for cht in os.environ.get("CHATS", "-1001500001979").split()]
WHITE_LIST   = [int(wht) for wht in os.environ.get("WHITE_LIST", "").split()]
BLACK_LIST   = [int(blk) for blk in os.environ.get("BLACK_LIST", "").split()]
DATABASE_URI = os.environ.get("DATABASE_URI", "mongodb+srv://CM:CM@cluster0.jfn3p38.mongodb.net/?retryWrites=true&w=majority")
PORT         = os.environ.get("PORT", "8080")

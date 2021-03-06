#!/usr/bin/env python
#
# $Id$
#
# PyXMLSec example: Verifying a file using keys manager.
#
# Verifies a file using keys manager
#
# Usage: 
#	verify2.py <signed-file> <public-pem-key1> [<public-pem-key2> [...]]
#
# Example:
#	./verify2.py sign1-res.xml rsapub.pem
#	./verify2.py sign2-res.xml rsapub.pem
#
# This is free software; see COPYING file in the source
# distribution for preciese wording.
# 
# Copyright (C) 2003-2004 Valery Febvre <vfebvre@easter-eggs.com>
#

import sys, os
sys.path.insert(0, '../')

import libxml2
import xmlsec

def main():
    assert(sys.argv)
    if len(sys.argv) < 3:
        print "Error: wrong number of arguments."
        print "Usage: %s <xml-file> <key-file1> [<key-file2> [...]]" % sys.argv[0]
        return sys.exit(1)
    
    # Init libxml library
    libxml2.initParser()
    libxml2.substituteEntitiesDefault(1)

    # Init xmlsec library
    if xmlsec.init() < 0:
        print "Error: xmlsec initialization failed."
        return sys.exit(-1)
    
    # Check loaded library version
    if xmlsec.checkVersion() != 1:
	print "Error: loaded xmlsec library version is not compatible.\n"
	sys.exit(-1)

    # Init crypto library
    if xmlsec.cryptoAppInit(None) < 0:
        print "Error: crypto initialization failed."
    
    # Init xmlsec-crypto library
    if xmlsec.cryptoInit() < 0:
        print "Error: xmlsec-crypto initialization failed."

    # Create keys manager and load keys
    mngr = load_keys(sys.argv[2:], len(sys.argv) - 2)

    res = 0
    # Verify file
    if mngr is not None:
        res = verify_file(mngr, sys.argv[1])
        # Destroy keys manager
        mngr.destroy()
    
    # Shutdown xmlsec-crypto library
    xmlsec.cryptoShutdown()

    # Shutdown crypto library
    xmlsec.cryptoAppShutdown()

    # Shutdown xmlsec library
    xmlsec.shutdown()

    # Shutdown LibXML2
    libxml2.cleanupParser()

    sys.exit(res)


# Creates simple keys manager and load PEM keys from files in it.
# The caller is responsible for destroing returned keys manager using destroy.
# Returns the newly created keys manager or None if an error occurs.
def load_keys(files, files_size):
    assert(files)
    assert(files_size > 0)

    # Create and initialize keys manager, we use a simple list based
    # keys manager, implement your own KeysStore klass if you need
    # something more sophisticated
    mngr = xmlsec.KeysMngr()
    if mngr is None:
        print "Error: failed to create keys manager."
        return None
    if xmlsec.cryptoAppDefaultKeysMngrInit(mngr) < 0:
        print "Error: failed to initialize keys manager."
        mngr.destroy()
        return None
    for file in files:
        # Load key
        if not check_filename(file):
            mngr.destroy()
            return None
        key = xmlsec.cryptoAppKeyLoad(file, xmlsec.KeyDataFormatPem,
                                      None, None, None)
        if key == None:
            print "Error: failed to load pem key from " + file
            mngr.destroy()        
            return None
        # Set key name to the file name, this is just an example!
        if key.setName(file) < 0:
            print "Error: failed to set key name for key from " + file
            key.destroy()
            mngr.destroy()
            return None
        # Add key to keys manager, from now on keys manager is responsible 
	# for destroying key
        if xmlsec.cryptoAppDefaultKeysMngrAdoptKey(mngr, key) < 0:
            print "Error: failed to add key from \"%s\" to keys manager" % file
            key.destroy()
            mngr.destroy()
            return None
    return mngr


# Verifies XML signature in xml_file.
# Returns 0 on success or a negative value if an error occurs.
def verify_file(mngr, xml_file):
    assert(mngr)
    assert(xml_file)

    # Load XML file
    if not check_filename(xml_file):
        return -1
    doc = libxml2.parseFile(xml_file)
    if doc is None or doc.getRootElement() is None:
	print "Error: unable to parse file \"%s\"" % tmpl_file
        return cleanup(doc)

    # Find start node
    node = xmlsec.findNode(doc.getRootElement(),
                           xmlsec.NodeSignature, xmlsec.DSigNs)
    if node is None:
        print "Error: start node not found in \"%s\"", xml_file

    # Create signature context
    dsig_ctx = xmlsec.DSigCtx(mngr)
    if dsig_ctx is None:
        print "Error: failed to create signature context"
        return cleanup(doc)

    # Verify signature
    if dsig_ctx.verify(node) < 0:
        print "Error: signature verify"
        return cleanup(doc, dsig_ctx)

    # Print verification result to stdout
    if dsig_ctx.status == xmlsec.DSigStatusSucceeded:
        print "Signature is OK"
    else:
        print "Signature is INVALID"

    # Success
    return cleanup(doc, dsig_ctx, 1)


def cleanup(doc=None, dsig_ctx=None, res=-1):
    if dsig_ctx is not None:
        dsig_ctx.destroy()
    if doc is not None:
        doc.freeDoc()
    return res


def check_filename(filename):
    if os.access(filename, os.R_OK):
        return 1
    else:
        print "Error: XML file \"%s\" not found OR no read access" % filename
        return 0


if __name__ == "__main__":
    main()

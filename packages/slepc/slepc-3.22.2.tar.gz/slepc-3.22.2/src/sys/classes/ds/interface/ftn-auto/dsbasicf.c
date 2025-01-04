#include "petscsys.h"
#include "petscfix.h"
#include "petsc/private/fortranimpl.h"
/* dsbasic.c */
/* Fortran interface file */

/*
* This file was generated automatically by bfort from the C source
* file.  
 */

#ifdef PETSC_USE_POINTER_CONVERSION
#if defined(__cplusplus)
extern "C" { 
#endif 
extern void *PetscToPointer(void*);
extern int PetscFromPointer(void *);
extern void PetscRmPointer(void*);
#if defined(__cplusplus)
} 
#endif 

#else

#define PetscToPointer(a) (a ? *(PetscFortranAddr *)(a) : 0)
#define PetscFromPointer(a) (PetscFortranAddr)(a)
#define PetscRmPointer(a)
#endif

#include "slepcds.h"
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define dscreate_ DSCREATE
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define dscreate_ dscreate
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define dssetoptionsprefix_ DSSETOPTIONSPREFIX
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define dssetoptionsprefix_ dssetoptionsprefix
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define dsappendoptionsprefix_ DSAPPENDOPTIONSPREFIX
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define dsappendoptionsprefix_ dsappendoptionsprefix
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define dsgetoptionsprefix_ DSGETOPTIONSPREFIX
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define dsgetoptionsprefix_ dsgetoptionsprefix
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define dssettype_ DSSETTYPE
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define dssettype_ dssettype
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define dsgettype_ DSGETTYPE
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define dsgettype_ dsgettype
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define dsduplicate_ DSDUPLICATE
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define dsduplicate_ dsduplicate
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define dssetmethod_ DSSETMETHOD
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define dssetmethod_ dssetmethod
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define dsgetmethod_ DSGETMETHOD
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define dsgetmethod_ dsgetmethod
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define dssetparallel_ DSSETPARALLEL
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define dssetparallel_ dssetparallel
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define dsgetparallel_ DSGETPARALLEL
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define dsgetparallel_ dsgetparallel
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define dssetcompact_ DSSETCOMPACT
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define dssetcompact_ dssetcompact
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define dsgetcompact_ DSGETCOMPACT
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define dsgetcompact_ dsgetcompact
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define dssetextrarow_ DSSETEXTRAROW
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define dssetextrarow_ dssetextrarow
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define dsgetextrarow_ DSGETEXTRAROW
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define dsgetextrarow_ dsgetextrarow
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define dssetrefined_ DSSETREFINED
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define dssetrefined_ dssetrefined
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define dsgetrefined_ DSGETREFINED
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define dsgetrefined_ dsgetrefined
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define dssetblocksize_ DSSETBLOCKSIZE
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define dssetblocksize_ dssetblocksize
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define dsgetblocksize_ DSGETBLOCKSIZE
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define dsgetblocksize_ dsgetblocksize
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define dssetfromoptions_ DSSETFROMOPTIONS
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define dssetfromoptions_ dssetfromoptions
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define dsview_ DSVIEW
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define dsview_ dsview
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define dsviewfromoptions_ DSVIEWFROMOPTIONS
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define dsviewfromoptions_ dsviewfromoptions
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define dsallocate_ DSALLOCATE
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define dsallocate_ dsallocate
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define dsreset_ DSRESET
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define dsreset_ dsreset
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define dsdestroy_ DSDESTROY
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define dsdestroy_ dsdestroy
#endif
/* Provide declarations for malloc/free if needed for strings */
#include <stdlib.h>


/* Definitions of Fortran Wrapper routines */
#if defined(__cplusplus)
extern "C" {
#endif
SLEPC_EXTERN void  dscreate_(MPI_Fint * comm,DS *newds, int *ierr)
{
PETSC_FORTRAN_OBJECT_CREATE(newds);
 PetscBool newds_null = !*(void**) newds ? PETSC_TRUE : PETSC_FALSE;
CHKFORTRANNULLOBJECT(newds);
*ierr = DSCreate(
	MPI_Comm_f2c(*(comm)),newds);
// if C routine nullifed the object, we must set to to -2 to indicate null set in Fortran
if (! newds_null && !*(void**) newds) * (void **) newds = (void *)-2;
}
SLEPC_EXTERN void  dssetoptionsprefix_(DS ds, char *prefix, int *ierr, PETSC_FORTRAN_CHARLEN_T cl0)
{
  char *_cltmp0 = PETSC_NULLPTR;
CHKFORTRANNULLOBJECT(ds);
/* insert Fortran-to-C conversion for prefix */
  FIXCHAR(prefix,cl0,_cltmp0);
*ierr = DSSetOptionsPrefix(
	(DS)PetscToPointer((ds) ),_cltmp0);
  FREECHAR(prefix,_cltmp0);
}
SLEPC_EXTERN void  dsappendoptionsprefix_(DS ds, char *prefix, int *ierr, PETSC_FORTRAN_CHARLEN_T cl0)
{
  char *_cltmp0 = PETSC_NULLPTR;
CHKFORTRANNULLOBJECT(ds);
/* insert Fortran-to-C conversion for prefix */
  FIXCHAR(prefix,cl0,_cltmp0);
*ierr = DSAppendOptionsPrefix(
	(DS)PetscToPointer((ds) ),_cltmp0);
  FREECHAR(prefix,_cltmp0);
}
SLEPC_EXTERN void  dsgetoptionsprefix_(DS ds, char *prefix, int *ierr, PETSC_FORTRAN_CHARLEN_T cl0)
{
  char *_cltmp0 = PETSC_NULLPTR;
CHKFORTRANNULLOBJECT(ds);
*ierr = DSGetOptionsPrefix(
	(DS)PetscToPointer((ds) ),(const char **)&_cltmp0);
/* insert C-to-Fortran conversion for prefix */
*ierr = PetscStrncpy(prefix, _cltmp0, cl0);
                        if (*ierr) return;
                        FIXRETURNCHAR(PETSC_TRUE, prefix, cl0);
}
SLEPC_EXTERN void  dssettype_(DS ds,char *type, int *ierr, PETSC_FORTRAN_CHARLEN_T cl0)
{
  char *_cltmp0 = PETSC_NULLPTR;
CHKFORTRANNULLOBJECT(ds);
/* insert Fortran-to-C conversion for type */
  FIXCHAR(type,cl0,_cltmp0);
*ierr = DSSetType(
	(DS)PetscToPointer((ds) ),_cltmp0);
  FREECHAR(type,_cltmp0);
}
SLEPC_EXTERN void  dsgettype_(DS ds,char *type, int *ierr, PETSC_FORTRAN_CHARLEN_T cl0)
{
  char *_cltmp0 = PETSC_NULLPTR;
CHKFORTRANNULLOBJECT(ds);
*ierr = DSGetType(
	(DS)PetscToPointer((ds) ),(const char **)&_cltmp0);
/* insert C-to-Fortran conversion for type */
*ierr = PetscStrncpy(type, _cltmp0, cl0);
                        if (*ierr) return;
                        FIXRETURNCHAR(PETSC_TRUE, type, cl0);
}
SLEPC_EXTERN void  dsduplicate_(DS ds,DS *dsnew, int *ierr)
{
CHKFORTRANNULLOBJECT(ds);
PetscBool dsnew_null = !*(void**) dsnew ? PETSC_TRUE : PETSC_FALSE;
CHKFORTRANNULLOBJECT(dsnew);
*ierr = DSDuplicate(
	(DS)PetscToPointer((ds) ),dsnew);
// if C routine nullifed the object, we must set to to -2 to indicate null set in Fortran
if (! dsnew_null && !*(void**) dsnew) * (void **) dsnew = (void *)-2;
}
SLEPC_EXTERN void  dssetmethod_(DS ds,PetscInt *meth, int *ierr)
{
CHKFORTRANNULLOBJECT(ds);
*ierr = DSSetMethod(
	(DS)PetscToPointer((ds) ),*meth);
}
SLEPC_EXTERN void  dsgetmethod_(DS ds,PetscInt *meth, int *ierr)
{
CHKFORTRANNULLOBJECT(ds);
CHKFORTRANNULLINTEGER(meth);
*ierr = DSGetMethod(
	(DS)PetscToPointer((ds) ),meth);
}
SLEPC_EXTERN void  dssetparallel_(DS ds,DSParallelType *pmode, int *ierr)
{
CHKFORTRANNULLOBJECT(ds);
*ierr = DSSetParallel(
	(DS)PetscToPointer((ds) ),*pmode);
}
SLEPC_EXTERN void  dsgetparallel_(DS ds,DSParallelType *pmode, int *ierr)
{
CHKFORTRANNULLOBJECT(ds);
*ierr = DSGetParallel(
	(DS)PetscToPointer((ds) ),pmode);
}
SLEPC_EXTERN void  dssetcompact_(DS ds,PetscBool *comp, int *ierr)
{
CHKFORTRANNULLOBJECT(ds);
*ierr = DSSetCompact(
	(DS)PetscToPointer((ds) ),*comp);
}
SLEPC_EXTERN void  dsgetcompact_(DS ds,PetscBool *comp, int *ierr)
{
CHKFORTRANNULLOBJECT(ds);
*ierr = DSGetCompact(
	(DS)PetscToPointer((ds) ),comp);
}
SLEPC_EXTERN void  dssetextrarow_(DS ds,PetscBool *ext, int *ierr)
{
CHKFORTRANNULLOBJECT(ds);
*ierr = DSSetExtraRow(
	(DS)PetscToPointer((ds) ),*ext);
}
SLEPC_EXTERN void  dsgetextrarow_(DS ds,PetscBool *ext, int *ierr)
{
CHKFORTRANNULLOBJECT(ds);
*ierr = DSGetExtraRow(
	(DS)PetscToPointer((ds) ),ext);
}
SLEPC_EXTERN void  dssetrefined_(DS ds,PetscBool *ref, int *ierr)
{
CHKFORTRANNULLOBJECT(ds);
*ierr = DSSetRefined(
	(DS)PetscToPointer((ds) ),*ref);
}
SLEPC_EXTERN void  dsgetrefined_(DS ds,PetscBool *ref, int *ierr)
{
CHKFORTRANNULLOBJECT(ds);
*ierr = DSGetRefined(
	(DS)PetscToPointer((ds) ),ref);
}
SLEPC_EXTERN void  dssetblocksize_(DS ds,PetscInt *bs, int *ierr)
{
CHKFORTRANNULLOBJECT(ds);
*ierr = DSSetBlockSize(
	(DS)PetscToPointer((ds) ),*bs);
}
SLEPC_EXTERN void  dsgetblocksize_(DS ds,PetscInt *bs, int *ierr)
{
CHKFORTRANNULLOBJECT(ds);
CHKFORTRANNULLINTEGER(bs);
*ierr = DSGetBlockSize(
	(DS)PetscToPointer((ds) ),bs);
}
SLEPC_EXTERN void  dssetfromoptions_(DS ds, int *ierr)
{
CHKFORTRANNULLOBJECT(ds);
*ierr = DSSetFromOptions(
	(DS)PetscToPointer((ds) ));
}
SLEPC_EXTERN void  dsview_(DS ds,PetscViewer viewer, int *ierr)
{
CHKFORTRANNULLOBJECT(ds);
CHKFORTRANNULLOBJECT(viewer);
*ierr = DSView(
	(DS)PetscToPointer((ds) ),PetscPatchDefaultViewers((PetscViewer*)viewer));
}
SLEPC_EXTERN void  dsviewfromoptions_(DS ds,PetscObject obj, char name[], int *ierr, PETSC_FORTRAN_CHARLEN_T cl0)
{
  char *_cltmp0 = PETSC_NULLPTR;
CHKFORTRANNULLOBJECT(ds);
CHKFORTRANNULLOBJECT(obj);
/* insert Fortran-to-C conversion for name */
  FIXCHAR(name,cl0,_cltmp0);
*ierr = DSViewFromOptions(
	(DS)PetscToPointer((ds) ),
	(PetscObject)PetscToPointer((obj) ),_cltmp0);
  FREECHAR(name,_cltmp0);
}
SLEPC_EXTERN void  dsallocate_(DS ds,PetscInt *ld, int *ierr)
{
CHKFORTRANNULLOBJECT(ds);
*ierr = DSAllocate(
	(DS)PetscToPointer((ds) ),*ld);
}
SLEPC_EXTERN void  dsreset_(DS ds, int *ierr)
{
CHKFORTRANNULLOBJECT(ds);
*ierr = DSReset(
	(DS)PetscToPointer((ds) ));
}
SLEPC_EXTERN void  dsdestroy_(DS *ds, int *ierr)
{
PETSC_FORTRAN_OBJECT_F_DESTROYED_TO_C_NULL(ds);
 PetscBool ds_null = !*(void**) ds ? PETSC_TRUE : PETSC_FALSE;
CHKFORTRANNULLOBJECT(ds);
*ierr = DSDestroy(ds);
// if C routine nullifed the object, we must set to to -2 to indicate null set in Fortran
if (! ds_null && !*(void**) ds) * (void **) ds = (void *)-2;
if (*ierr) return;
PETSC_FORTRAN_OBJECT_C_NULL_TO_F_DESTROYED(ds);
 }
#if defined(__cplusplus)
}
#endif
